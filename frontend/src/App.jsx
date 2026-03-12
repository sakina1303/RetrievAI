import React from 'react'
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom'
import { ToastContainer } from 'react-toastify'
import 'react-toastify/dist/ReactToastify.css'
import { AuthProvider } from './context/AuthContext'
import Layout from './components/Layout'
import Login from './pages/Login'
import Register from './pages/Register'
import Dashboard from './pages/Dashboard'
import ReportLostItem from './pages/ReportLostItem'
import ReportFoundItem from './pages/ReportFoundItem'
import LostItems from './pages/LostItems'
import FoundItems from './pages/FoundItems'
import MyClaims from './pages/MyClaims'
import AdminDashboard from './pages/AdminDashboard'
import PrivateRoute from './components/PrivateRoute'
import AdminRoute from './components/AdminRoute'

function App() {
  return (
    <AuthProvider>
      <Router>
        <Layout>
          <Routes>
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />
            
            <Route path="/dashboard" element={
              <PrivateRoute>
                <Dashboard />
              </PrivateRoute>
            } />
            
            <Route path="/report-lost" element={
              <PrivateRoute>
                <ReportLostItem />
              </PrivateRoute>
            } />
            
            <Route path="/report-found" element={
              <PrivateRoute>
                <ReportFoundItem />
              </PrivateRoute>
            } />
            
            <Route path="/lost-items" element={
              <PrivateRoute>
                <LostItems />
              </PrivateRoute>
            } />
            
            <Route path="/found-items" element={
              <PrivateRoute>
                <FoundItems />
              </PrivateRoute>
            } />
            
            <Route path="/my-claims" element={
              <PrivateRoute>
                <MyClaims />
              </PrivateRoute>
            } />
            
            <Route path="/admin" element={
              <AdminRoute>
                <AdminDashboard />
              </AdminRoute>
            } />
            
            <Route path="/" element={<Navigate to="/dashboard" />} />
          </Routes>
        </Layout>
      </Router>
      <ToastContainer position="top-right" autoClose={3000} />
    </AuthProvider>
  )
}

export default App
