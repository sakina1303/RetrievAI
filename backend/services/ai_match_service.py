import os
from typing import List, Dict
from config import Config

class AIMatchService:
    """
    AI-powered matching service for lost and found items.
    Supports both Gemini and OpenAI APIs for text similarity matching.
    """
    
    def __init__(self):
        self.provider = Config.AI_PROVIDER
        self.similarity_threshold = Config.SIMILARITY_THRESHOLD
        
        if self.provider == 'gemini':
            self._init_gemini()
        elif self.provider == 'openai':
            self._init_openai()
    
    def _init_gemini(self):
        """Initialize Gemini API client"""
        try:
            import google.generativeai as genai
            genai.configure(api_key=Config.GEMINI_API_KEY)
            self.model = genai.GenerativeModel('gemini-pro')
        except Exception as e:
            print(f"Warning: Gemini API not configured: {e}")
            self.model = None
    
    def _init_openai(self):
        """Initialize OpenAI API client"""
        try:
            from openai import OpenAI
            self.client = OpenAI(api_key=Config.OPENAI_API_KEY)
        except Exception as e:
            print(f"Warning: OpenAI API not configured: {e}")
            self.client = None
    
    def calculate_text_similarity(self, text1: str, text2: str) -> float:
        """
        Calculate similarity score between two text descriptions.
        Returns a score between 0 and 1.
        """
        if self.provider == 'gemini':
            return self._calculate_similarity_gemini(text1, text2)
        elif self.provider == 'openai':
            return self._calculate_similarity_openai(text1, text2)
        else:
            # Fallback to basic string matching
            return self._calculate_similarity_basic(text1, text2)
    
    def _calculate_similarity_gemini(self, text1: str, text2: str) -> float:
        """Calculate similarity using Gemini API"""
        if not self.model:
            return self._calculate_similarity_basic(text1, text2)
        
        try:
            prompt = f"""
            Compare these two item descriptions and rate their similarity on a scale of 0 to 1.
            0 means completely different items, 1 means identical items.
            
            Description 1: {text1}
            Description 2: {text2}
            
            Respond with ONLY a number between 0 and 1. No explanations.
            """
            
            response = self.model.generate_content(prompt)
            score = float(response.text.strip())
            return max(0.0, min(1.0, score))
        except Exception as e:
            print(f"Gemini API error: {e}")
            return self._calculate_similarity_basic(text1, text2)
    
    def _calculate_similarity_openai(self, text1: str, text2: str) -> float:
        """Calculate similarity using OpenAI API"""
        if not self.client:
            return self._calculate_similarity_basic(text1, text2)
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a similarity matching assistant. Rate similarity between 0 and 1."},
                    {"role": "user", "content": f"Compare:\n1: {text1}\n2: {text2}\nRate 0-1:"}
                ],
                temperature=0.3,
                max_tokens=10
            )
            score = float(response.choices[0].message.content.strip())
            return max(0.0, min(1.0, score))
        except Exception as e:
            print(f"OpenAI API error: {e}")
            return self._calculate_similarity_basic(text1, text2)
    
    def _calculate_similarity_basic(self, text1: str, text2: str) -> float:
        """Basic similarity calculation using word overlap (fallback)"""
        words1 = set(text1.lower().split())
        words2 = set(text2.lower().split())
        
        if not words1 or not words2:
            return 0.0
        
        intersection = words1.intersection(words2)
        union = words1.union(words2)
        
        return len(intersection) / len(union) if union else 0.0
    
    def find_matches_for_lost_item(self, lost_item, found_items: List) -> List[Dict]:
        """
        Find matching found items for a lost item.
        Returns a list of matches with similarity scores.
        """
        matches = []
        
        lost_text = f"{lost_item.name} {lost_item.description} {lost_item.location}"
        
        for found_item in found_items:
            if found_item.status != 'available':
                continue
            
            found_text = f"{found_item.name} {found_item.description} {found_item.location}"
            
            similarity_score = self.calculate_text_similarity(lost_text, found_text)
            
            if similarity_score >= self.similarity_threshold:
                matches.append({
                    'found_item': found_item.to_dict(),
                    'similarity_score': round(similarity_score, 2),
                    'match_confidence': self._get_confidence_label(similarity_score)
                })
        
        # Sort by similarity score (highest first)
        matches.sort(key=lambda x: x['similarity_score'], reverse=True)
        
        return matches
    
    def find_matches_for_found_item(self, found_item, lost_items: List) -> List[Dict]:
        """
        Find matching lost items for a found item.
        Returns a list of matches with similarity scores.
        """
        matches = []
        
        found_text = f"{found_item.name} {found_item.description} {found_item.location}"
        
        for lost_item in lost_items:
            if lost_item.status not in ['active', 'matched']:
                continue
            
            lost_text = f"{lost_item.name} {lost_item.description} {lost_item.location}"
            
            similarity_score = self.calculate_text_similarity(found_text, lost_text)
            
            if similarity_score >= self.similarity_threshold:
                matches.append({
                    'lost_item': lost_item.to_dict(),
                    'similarity_score': round(similarity_score, 2),
                    'match_confidence': self._get_confidence_label(similarity_score)
                })
        
        # Sort by similarity score (highest first)
        matches.sort(key=lambda x: x['similarity_score'], reverse=True)
        
        return matches
    
    def _get_confidence_label(self, score: float) -> str:
        """Convert numerical score to confidence label"""
        if score >= 0.9:
            return "Very High"
        elif score >= 0.8:
            return "High"
        elif score >= 0.7:
            return "Medium"
        else:
            return "Low"
