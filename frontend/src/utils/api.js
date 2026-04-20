import axios from 'axios'

const getApiBaseUrl = () => {
  const envUrl = import.meta.env.VITE_API_BASE_URL;
  if (import.meta.env.PROD) {
    if (envUrl) {
      return envUrl.endsWith('/api') ? envUrl : `${envUrl}/api`;
    }
    return '/api'; // Default relative path for production
  }
  return envUrl || 'http://localhost:5001/api';
};

const API_BASE_URL = getApiBaseUrl();
const API_ORIGIN = API_BASE_URL.startsWith('/') && !API_BASE_URL.startsWith('http') 
  ? '' 
  : API_BASE_URL.replace(/\/api\/?$/, '');

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Add token to requests
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// Handle auth/session failures in one place.
api.interceptors.response.use(
  (response) => response,
  (error) => {
    const status = error?.response?.status
    const path = error?.config?.url || ''
    const details = `${error?.response?.data?.error || ''} ${error?.response?.data?.msg || ''}`.toLowerCase()
    const isAuthPath = path.includes('/auth/login') || path.includes('/auth/register')
    const looksLikeTokenError = details.includes('token') || details.includes('subject') || status === 422

    if (!isAuthPath && (status === 401 || looksLikeTokenError)) {
      localStorage.removeItem('token')
      if (window.location.pathname !== '/login') {
        window.location.href = '/login'
      }
    }

    return Promise.reject(error)
  }
)

export const buildImageUrl = (imageName) => {
  if (!imageName) return ''
  if (imageName.startsWith('http://') || imageName.startsWith('https://')) {
    return imageName
  }
  return `${API_ORIGIN}/uploads/${imageName}`
}

// Auth APIs
export const authAPI = {
  register: (data) => api.post('/auth/register', data),
  login: (data) => api.post('/auth/login', data),
  getCurrentUser: () => api.get('/auth/me'),
}

// Item APIs
export const itemAPI = {
  createLostItem: (formData) => {
    const config = { headers: { 'Content-Type': 'multipart/form-data' } }
    return api.post('/items/lost', formData, config)
  },
  createFoundItem: (formData) => {
    const config = { headers: { 'Content-Type': 'multipart/form-data' } }
    return api.post('/items/found', formData, config)
  },
  getAllLostItems: () => api.get('/items/lost'),
  getAllFoundItems: () => api.get('/items/found'),
  getMyLostItems: () => api.get('/items/my-lost-items'),
  getMyFoundItems: () => api.get('/items/my-found-items'),
  getLostItemMatches: (id) => api.get(`/items/lost/${id}/matches`),
  getFoundItemMatches: (id) => api.get(`/items/found/${id}/matches`),
  deleteLostItem: (id) => api.delete(`/items/lost/${id}`),
  deleteFoundItem: (id) => api.delete(`/items/found/${id}`),
}

// Claim APIs
export const claimAPI = {
  createClaim: (data) => api.post('/claims/', data),
  getMyClaims: () => api.get('/claims/my-claims'),
  getClaim: (id) => api.get(`/claims/${id}`),
}

// Admin APIs
export const adminAPI = {
  getAllUsers: () => api.get('/admin/users'),
  getAllClaims: () => api.get('/admin/claims'),
  getPendingClaims: () => api.get('/admin/claims/pending'),
  approveClaim: (id) => api.post(`/admin/claims/${id}/approve`),
  rejectClaim: (id) => api.post(`/admin/claims/${id}/reject`),
  getAllLostItems: () => api.get('/admin/items/lost'),
  getAllFoundItems: () => api.get('/admin/items/found'),
}

export default api
