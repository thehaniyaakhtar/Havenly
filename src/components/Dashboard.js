import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { 
  TrendingUp, 
  TrendingDown, 
  DollarSign, 
  Shield, 
  Users, 
  Heart,
  BarChart3,
  PieChart,
  Activity,
  Calendar,
  Target,
  Award
} from 'lucide-react';
import { 
  LineChart, 
  Line, 
  XAxis, 
  YAxis, 
  CartesianGrid, 
  Tooltip, 
  ResponsiveContainer, 
  PieChart as RechartsPieChart, 
  Pie, 
  Cell,
  BarChart,
  Bar,
  AreaChart,
  Area
} from 'recharts';

const Dashboard = () => {
  const [activeTab, setActiveTab] = useState('overview');
  const [timeRange, setTimeRange] = useState('month');

  // Sample data for charts
  const premiumData = [
    { month: 'Jan', premium: 320, claims: 280, savings: 40 },
    { month: 'Feb', premium: 315, claims: 290, savings: 25 },
    { month: 'Mar', premium: 310, claims: 275, savings: 35 },
    { month: 'Apr', premium: 305, claims: 300, savings: 5 },
    { month: 'May', premium: 300, claims: 265, savings: 35 },
    { month: 'Jun', premium: 295, claims: 280, savings: 15 },
  ];

  const planDistributionData = [
    { name: 'Bronze', value: 35, color: '#cd7f32' },
    { name: 'Silver', value: 40, color: '#c0c0c0' },
    { name: 'Gold', value: 20, color: '#ffd700' },
    { name: 'Platinum', value: 5, color: '#e5e4e2' },
  ];

  const claimsData = [
    { category: 'Preventive', amount: 45, color: '#10b981' },
    { category: 'Emergency', amount: 25, color: '#ef4444' },
    { category: 'Specialist', amount: 20, color: '#3b82f6' },
    { category: 'Prescription', amount: 10, color: '#8b5cf6' },
  ];

  const metrics = [
    {
      title: 'Monthly Premium',
      value: '₹320',
      change: '+2.5%',
      trend: 'up',
      icon: DollarSign,
      color: 'text-green-600'
    },
    {
      title: 'Total Claims',
      value: '₹280',
      change: '-5.2%',
      trend: 'down',
      icon: Shield,
      color: 'text-blue-600'
    },
    {
      title: 'Net Savings',
      value: '₹40',
      change: '+12.8%',
      trend: 'up',
      icon: TrendingUp,
      color: 'text-purple-600'
    },
    {
      title: 'Coverage Score',
      value: '92%',
      change: '+3.1%',
      trend: 'up',
      icon: Heart,
      color: 'text-red-600'
    }
  ];

  const recentActivities = [
    {
      type: 'Claim Submitted',
      description: 'Annual physical examination',
      amount: '₹1,200',
      date: '2 hours ago',
      status: 'pending'
    },
    {
      type: 'Premium Paid',
      description: 'Monthly premium payment',
      amount: '₹320',
      date: '1 day ago',
      status: 'completed'
    },
    {
      type: 'Plan Updated',
      description: 'Added dental coverage',
      amount: '+₹50',
      date: '3 days ago',
      status: 'completed'
    },
    {
      type: 'Claim Processed',
      description: 'Prescription medication',
      amount: '₹85',
      date: '1 week ago',
      status: 'completed'
    }
  ];

  const goals = [
    {
      title: 'Emergency Fund',
      target: 50000,
      current: 35000,
      icon: Target,
      color: 'bg-blue-500'
    },
    {
      title: 'Health Savings',
      target: 25000,
      current: 18000,
      icon: Heart,
      color: 'bg-green-500'
    },
    {
      title: 'Premium Reduction',
      target: 50,
      current: 25,
      icon: TrendingDown,
      color: 'bg-purple-500'
    }
  ];

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-gray-900 mb-2">Insurance Dashboard</h1>
          <p className="text-gray-600">Track your coverage, claims, and savings in one place</p>
        </div>

        {/* Metrics Cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
          {metrics.map((metric, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: index * 0.1 }}
              className="card"
            >
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-sm font-medium text-gray-600">{metric.title}</p>
                  <p className="text-2xl font-bold text-gray-900">{metric.value}</p>
                  <div className="flex items-center mt-1">
                    {metric.trend === 'up' ? (
                      <TrendingUp className="h-4 w-4 text-green-500 mr-1" />
                    ) : (
                      <TrendingDown className="h-4 w-4 text-red-500 mr-1" />
                    )}
                    <span className={`text-sm ${metric.trend === 'up' ? 'text-green-600' : 'text-red-600'}`}>
                      {metric.change}
                    </span>
                  </div>
                </div>
                <div className={`p-3 rounded-full bg-gray-100 ${metric.color}`}>
                  <metric.icon className="h-6 w-6" />
                </div>
              </div>
            </motion.div>
          ))}
        </div>

        {/* Tabs */}
        <div className="mb-8">
          <div className="border-b border-gray-200">
            <nav className="-mb-px flex space-x-8">
              {['overview', 'analytics', 'goals', 'activity'].map((tab) => (
                <button
                  key={tab}
                  onClick={() => setActiveTab(tab)}
                  className={`py-2 px-1 border-b-2 font-medium text-sm capitalize ${
                    activeTab === tab
                      ? 'border-primary-500 text-primary-600'
                      : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
                  }`}
                >
                  {tab}
                </button>
              ))}
            </nav>
          </div>
        </div>

        {/* Tab Content */}
        {activeTab === 'overview' && (
          <div className="grid lg:grid-cols-2 gap-8">
            {/* Premium Trends */}
            <motion.div
              initial={{ opacity: 0, x: -30 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ duration: 0.6 }}
              className="card"
            >
              <div className="flex items-center justify-between mb-6">
                <h3 className="text-xl font-semibold">Premium & Claims Trend</h3>
                <select
                  value={timeRange}
                  onChange={(e) => setTimeRange(e.target.value)}
                  className="px-3 py-1 border border-gray-300 rounded-md text-sm"
                >
                  <option value="week">Week</option>
                  <option value="month">Month</option>
                  <option value="quarter">Quarter</option>
                  <option value="year">Year</option>
                </select>
              </div>
              <ResponsiveContainer width="100%" height={300}>
                <AreaChart data={premiumData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="month" />
                  <YAxis />
                  <Tooltip />
                  <Area type="monotone" dataKey="premium" stackId="1" stroke="#3b82f6" fill="#3b82f6" fillOpacity={0.3} />
                  <Area type="monotone" dataKey="claims" stackId="1" stroke="#ef4444" fill="#ef4444" fillOpacity={0.3} />
                </AreaChart>
              </ResponsiveContainer>
            </motion.div>

            {/* Plan Distribution */}
            <motion.div
              initial={{ opacity: 0, x: 30 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ duration: 0.6, delay: 0.2 }}
              className="card"
            >
              <h3 className="text-xl font-semibold mb-6">Plan Distribution</h3>
              <ResponsiveContainer width="100%" height={300}>
                <RechartsPieChart>
                  <Pie
                    data={planDistributionData}
                    cx="50%"
                    cy="50%"
                    outerRadius={80}
                    dataKey="value"
                    label={({ name, percent }) => `${name} ${(percent * 100).toFixed(0)}%`}
                  >
                    {planDistributionData.map((entry, index) => (
                      <Cell key={`cell-${index}`} fill={entry.color} />
                    ))}
                  </Pie>
                  <Tooltip />
                </RechartsPieChart>
              </ResponsiveContainer>
            </motion.div>
          </div>
        )}

        {activeTab === 'analytics' && (
          <div className="grid lg:grid-cols-2 gap-8">
            {/* Claims Breakdown */}
            <motion.div
              initial={{ opacity: 0, y: 30 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6 }}
              className="card"
            >
              <h3 className="text-xl font-semibold mb-6">Claims Breakdown</h3>
              <ResponsiveContainer width="100%" height={300}>
                <BarChart data={claimsData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="category" />
                  <YAxis />
                  <Tooltip />
                  <Bar dataKey="amount" fill="#3b82f6" />
                </BarChart>
              </ResponsiveContainer>
            </motion.div>

            {/* Savings Trend */}
            <motion.div
              initial={{ opacity: 0, y: 30 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: 0.2 }}
              className="card"
            >
              <h3 className="text-xl font-semibold mb-6">Monthly Savings</h3>
              <ResponsiveContainer width="100%" height={300}>
                <LineChart data={premiumData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="month" />
                  <YAxis />
                  <Tooltip />
                  <Line type="monotone" dataKey="savings" stroke="#10b981" strokeWidth={3} />
                </LineChart>
              </ResponsiveContainer>
            </motion.div>
          </div>
        )}

        {activeTab === 'goals' && (
          <div className="grid lg:grid-cols-3 gap-6">
            {goals.map((goal, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 30 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.6, delay: index * 0.1 }}
                className="card"
              >
                <div className="flex items-center mb-4">
                  <div className={`p-3 rounded-full ${goal.color} mr-4`}>
                    <goal.icon className="h-6 w-6 text-white" />
                  </div>
                  <div>
                    <h3 className="text-lg font-semibold">{goal.title}</h3>
                    <p className="text-sm text-gray-600">
                      ₹{goal.current.toLocaleString()} / ₹{goal.target.toLocaleString()}
                    </p>
                  </div>
                </div>
                <div className="w-full bg-gray-200 rounded-full h-2 mb-4">
                  <div
                    className="bg-primary-600 h-2 rounded-full transition-all duration-300"
                    style={{ width: `${(goal.current / goal.target) * 100}%` }}
                  ></div>
                </div>
                <p className="text-sm text-gray-600">
                  {Math.round((goal.current / goal.target) * 100)}% complete
                </p>
              </motion.div>
            ))}
          </div>
        )}

        {activeTab === 'activity' && (
          <div className="card">
            <h3 className="text-xl font-semibold mb-6">Recent Activity</h3>
            <div className="space-y-4">
              {recentActivities.map((activity, index) => (
                <motion.div
                  key={index}
                  initial={{ opacity: 0, x: -30 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ duration: 0.6, delay: index * 0.1 }}
                  className="flex items-center justify-between p-4 bg-gray-50 rounded-lg"
                >
                  <div className="flex items-center">
                    <div className={`w-3 h-3 rounded-full mr-4 ${
                      activity.status === 'completed' ? 'bg-green-500' : 'bg-yellow-500'
                    }`}></div>
                    <div>
                      <p className="font-medium text-gray-900">{activity.type}</p>
                      <p className="text-sm text-gray-600">{activity.description}</p>
                    </div>
                  </div>
                  <div className="text-right">
                    <p className="font-medium text-gray-900">{activity.amount}</p>
                    <p className="text-sm text-gray-500">{activity.date}</p>
                  </div>
                </motion.div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default Dashboard; 