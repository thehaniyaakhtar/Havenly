import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { motion } from 'framer-motion';
import { 
  Shield, 
  Heart, 
  Users, 
  TrendingUp, 
  CheckCircle, 
  Star,
  ArrowRight,
  Play,
  Phone,
  Mail,
  MapPin,
  Calculator,
  Award,
  Clock,
  Zap
} from 'lucide-react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, PieChart, Pie, Cell } from 'recharts';

const HomePage = () => {
  const [currentFeature, setCurrentFeature] = useState(0);
  const [stats, setStats] = useState({
    plans: 0,
    users: 0,
    savings: 0,
    satisfaction: 0
  });

  // Animated stats
  useEffect(() => {
    const targetStats = { plans: 1500, users: 50000, savings: 2500000, satisfaction: 98 };
    const duration = 2000;
    const steps = 60;
    const increment = duration / steps;

    let currentStep = 0;
    const timer = setInterval(() => {
      currentStep++;
      const progress = currentStep / steps;
      
      setStats({
        plans: Math.floor(targetStats.plans * progress),
        users: Math.floor(targetStats.users * progress),
        savings: Math.floor(targetStats.savings * progress),
        satisfaction: Math.floor(targetStats.satisfaction * progress)
      });

      if (currentStep >= steps) {
        clearInterval(timer);
      }
    }, increment);

    return () => clearInterval(timer);
  }, []);

  // Sample data for charts
  const priceTrendData = [
    { month: 'Jan', average: 320, premium: 450 },
    { month: 'Feb', average: 315, premium: 440 },
    { month: 'Mar', average: 310, premium: 430 },
    { month: 'Apr', average: 305, premium: 425 },
    { month: 'May', average: 300, premium: 420 },
    { month: 'Jun', average: 295, premium: 415 },
  ];

  const planDistributionData = [
    { name: 'Bronze', value: 35, color: '#cd7f32' },
    { name: 'Silver', value: 40, color: '#c0c0c0' },
    { name: 'Gold', value: 20, color: '#ffd700' },
    { name: 'Platinum', value: 5, color: '#e5e4e2' },
  ];

  const features = [
    {
      icon: <Shield className="h-8 w-8" />,
      title: "AI-Powered Matching",
      description: "Our advanced AI analyzes your needs and finds the perfect plan match."
    },
    {
      icon: <Calculator className="h-8 w-8" />,
      title: "Smart Cost Analysis",
      description: "Compare premiums, deductibles, and out-of-pocket costs side by side."
    },
    {
      icon: <Heart className="h-8 w-8" />,
      title: "Health-First Approach",
      description: "Plans that prioritize your health with wellness programs and preventive care."
    },
    {
      icon: <Users className="h-8 w-8" />,
      title: "Family Coverage",
      description: "Comprehensive family plans that grow with your changing needs."
    }
  ];

  const testimonials = [
    {
      name: "Sarah Johnson",
      role: "Small Business Owner",
      content: "Havenly helped me find a plan that actually fits my budget and covers what I need. The AI recommendations were spot-on!",
      rating: 5
    },
    {
      name: "Michael Chen",
      role: "Family of 4",
      content: "Switching our family insurance was a breeze. The comparison tools made it easy to see exactly what we were getting.",
      rating: 5
    },
    {
      name: "Emily Rodriguez",
      role: "Freelancer",
      content: "As a freelancer, I was worried about finding affordable coverage. Havenly found me a great plan with dental included!",
      rating: 5
    }
  ];

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="hero-gradient text-white relative overflow-hidden">
        <div className="absolute inset-0 bg-black opacity-20"></div>
        <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24">
          <div className="grid lg:grid-cols-2 gap-12 items-center">
            <motion.div
              initial={{ opacity: 0, x: -50 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ duration: 0.8 }}
            >
              <h1 className="text-5xl lg:text-6xl font-bold mb-6">
                Not just policies — 
                <span className="block text-yellow-300">a plan that fits right</span>
              </h1>
              <p className="text-xl mb-8 text-gray-100">
                Because whether you're starting out or starting over — we've got you covered with AI-powered insurance recommendations.
              </p>
              <div className="flex flex-col sm:flex-row gap-4">
                <Link to="/find-plan" className="btn-primary text-center">
                  Find Your Plan
                  <ArrowRight className="h-4 w-4 ml-2" />
                </Link>
                <button className="btn-secondary text-center">
                  <Play className="h-4 w-4 mr-2" />
                  Watch Demo
                </button>
              </div>
            </motion.div>
            <motion.div
              initial={{ opacity: 0, x: 50 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ duration: 0.8, delay: 0.2 }}
              className="relative"
            >
              <div className="bg-white/10 backdrop-blur-sm rounded-2xl p-8 animate-float">
                <div className="text-center">
                  <Shield className="h-16 w-16 mx-auto mb-4 text-yellow-300" />
                  <h3 className="text-xl font-semibold mb-2">AI Insurance Advisor</h3>
                  <p className="text-gray-200">Get personalized recommendations in seconds</p>
                </div>
              </div>
            </motion.div>
          </div>
        </div>
      </section>

      {/* Stats Section */}
      <section className="py-16 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-2 lg:grid-cols-4 gap-8">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6 }}
              className="text-center"
            >
              <div className="text-3xl font-bold text-primary-600 mb-2">{stats.plans.toLocaleString()}+</div>
              <div className="text-gray-600">Available Plans</div>
            </motion.div>
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: 0.1 }}
              className="text-center"
            >
              <div className="text-3xl font-bold text-primary-600 mb-2">{stats.users.toLocaleString()}+</div>
              <div className="text-gray-600">Happy Customers</div>
            </motion.div>
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: 0.2 }}
              className="text-center"
            >
              <div className="text-3xl font-bold text-primary-600 mb-2">₹{stats.savings.toLocaleString()}</div>
              <div className="text-gray-600">Total Savings</div>
            </motion.div>
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: 0.3 }}
              className="text-center"
            >
              <div className="text-3xl font-bold text-primary-600 mb-2">{stats.satisfaction}%</div>
              <div className="text-gray-600">Satisfaction Rate</div>
            </motion.div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-20 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold text-gray-900 mb-4">How we help you</h2>
            <p className="text-xl text-gray-600 max-w-3xl mx-auto">
              Explore plans that make sense for your life and your budget with our comprehensive tools and AI assistance.
            </p>
          </div>
          
          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
            {features.map((feature, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 30 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.6, delay: index * 0.1 }}
                className="card text-center group hover:scale-105"
              >
                <div className="text-primary-600 mb-4 group-hover:scale-110 transition-transform">
                  {feature.icon}
                </div>
                <h3 className="text-xl font-semibold mb-3">{feature.title}</h3>
                <p className="text-gray-600">{feature.description}</p>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Charts Section */}
      <section className="py-20 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold text-gray-900 mb-4">Market Insights</h2>
            <p className="text-xl text-gray-600">Stay informed with real-time market data and trends</p>
          </div>
          
          <div className="grid lg:grid-cols-2 gap-12">
            <motion.div
              initial={{ opacity: 0, x: -30 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ duration: 0.8 }}
              className="card"
            >
              <h3 className="text-2xl font-semibold mb-6">Premium Trends</h3>
              <ResponsiveContainer width="100%" height={300}>
                <LineChart data={priceTrendData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="month" />
                  <YAxis />
                  <Tooltip />
                  <Line type="monotone" dataKey="average" stroke="#3b82f6" strokeWidth={3} />
                  <Line type="monotone" dataKey="premium" stroke="#ef4444" strokeWidth={3} />
                </LineChart>
              </ResponsiveContainer>
            </motion.div>
            
            <motion.div
              initial={{ opacity: 0, x: 30 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ duration: 0.8, delay: 0.2 }}
              className="card"
            >
              <h3 className="text-2xl font-semibold mb-6">Plan Distribution</h3>
              <ResponsiveContainer width="100%" height={300}>
                <PieChart>
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
                </PieChart>
              </ResponsiveContainer>
            </motion.div>
          </div>
        </div>
      </section>

      {/* Testimonials Section */}
      <section className="py-20 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold text-gray-900 mb-4">What our customers say</h2>
            <p className="text-xl text-gray-600">Real stories from real people who found their perfect plan</p>
          </div>
          
          <div className="grid md:grid-cols-3 gap-8">
            {testimonials.map((testimonial, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 30 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.6, delay: index * 0.2 }}
                className="card"
              >
                <div className="flex mb-4">
                  {[...Array(testimonial.rating)].map((_, i) => (
                    <Star key={i} className="h-5 w-5 text-yellow-400 fill-current" />
                  ))}
                </div>
                <p className="text-gray-600 mb-6 italic">"{testimonial.content}"</p>
                <div>
                  <div className="font-semibold text-gray-900">{testimonial.name}</div>
                  <div className="text-sm text-gray-500">{testimonial.role}</div>
                </div>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 bg-primary-600 text-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
          >
            <h2 className="text-4xl font-bold mb-6">Ready to find your perfect plan?</h2>
            <p className="text-xl mb-8 text-primary-100">
              Join thousands of customers who've already found their ideal insurance coverage
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Link to="/find-plan" className="btn-primary bg-white text-primary-600 hover:bg-gray-100">
                Start Your Search
                <ArrowRight className="h-4 w-4 ml-2" />
              </Link>
              <button className="btn-secondary border-white text-white hover:bg-white hover:text-primary-600">
                <Phone className="h-4 w-4 mr-2" />
                Talk to Expert
              </button>
            </div>
          </motion.div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-900 text-white py-12">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid md:grid-cols-4 gap-8">
            <div>
              <div className="flex items-center space-x-2 mb-4">
                <Shield className="h-8 w-8 text-primary-400" />
                <span className="text-xl font-bold">Havenly</span>
              </div>
              <p className="text-gray-400">
                AI-powered insurance advisor helping you find the perfect coverage for your needs.
              </p>
            </div>
            <div>
              <h3 className="font-semibold mb-4">Quick Links</h3>
              <ul className="space-y-2 text-gray-400">
                <li><Link to="/find-plan" className="hover:text-white">Find Plans</Link></li>
                <li><Link to="/dashboard" className="hover:text-white">Dashboard</Link></li>
                <li><Link to="/about" className="hover:text-white">About Us</Link></li>
              </ul>
            </div>
            <div>
              <h3 className="font-semibold mb-4">Support</h3>
              <ul className="space-y-2 text-gray-400">
                <li className="flex items-center"><Phone className="h-4 w-4 mr-2" />1-800-HAVENLY</li>
                <li className="flex items-center"><Mail className="h-4 w-4 mr-2" />support@havenly.com</li>
                <li className="flex items-center"><MapPin className="h-4 w-4 mr-2" />24/7 Online Support</li>
              </ul>
            </div>
            <div>
              <h3 className="font-semibold mb-4">Features</h3>
              <ul className="space-y-2 text-gray-400">
                <li className="flex items-center"><Zap className="h-4 w-4 mr-2" />AI Matching</li>
                <li className="flex items-center"><Calculator className="h-4 w-4 mr-2" />Cost Analysis</li>
                <li className="flex items-center"><Clock className="h-4 w-4 mr-2" />Real-time Quotes</li>
              </ul>
            </div>
          </div>
          <div className="border-t border-gray-800 mt-8 pt-8 text-center text-gray-400">
            <p>&copy; 2024 Havenly. All rights reserved.</p>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default HomePage; 