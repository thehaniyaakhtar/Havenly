import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { Search, Filter, Shield, Heart, Users, Calculator, ArrowRight, CheckCircle } from 'lucide-react';
import toast from 'react-hot-toast';

const PlanFinder = () => {
  const [formData, setFormData] = useState({
    ageGroup: '',
    tobacco: '',
    planType: '',
    state: '',
    needs: []
  });
  const [isLoading, setIsLoading] = useState(false);
  const [results, setResults] = useState(null);

  const ageGroups = ["18-25", "26-35", "36-45", "46-60", "61+"];
  const planTypes = ["Individual", "Family", "Child-only"];
  const states = ["Any", "CA", "NY", "TX", "FL", "IL", "PA", "OH", "GA", "NC", "MI"];
  const coverageNeeds = ["Wellness", "Maternity", "Mental Health", "Dental"];

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    
    try {
      // This would integrate with your Streamlit backend
      // For now, we'll simulate the API call
      await new Promise(resolve => setTimeout(resolve, 2000));
      
      // Simulated results
      setResults([
        {
          name: "Blue Cross Blue Shield Gold",
          metalLevel: "Gold",
          planType: "PPO",
          cost: 450,
          wellness: "Yes",
          maternity: "Yes",
          mentalHealth: "Yes",
          matchScore: 4
        },
        {
          name: "Aetna Silver Choice",
          metalLevel: "Silver",
          planType: "HMO",
          cost: 320,
          wellness: "Yes",
          maternity: "No",
          mentalHealth: "Yes",
          matchScore: 3
        },
        {
          name: "Cigna Bronze Plus",
          metalLevel: "Bronze",
          planType: "EPO",
          cost: 280,
          wellness: "No",
          maternity: "Yes",
          mentalHealth: "No",
          matchScore: 2
        }
      ]);
      
      toast.success('Found matching plans!');
    } catch (error) {
      toast.error('Error finding plans. Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  const handleInputChange = (field, value) => {
    setFormData(prev => ({
      ...prev,
      [field]: value
    }));
  };

  const handleNeedsChange = (need) => {
    setFormData(prev => ({
      ...prev,
      needs: prev.needs.includes(need)
        ? prev.needs.filter(n => n !== need)
        : [...prev.needs, need]
    }));
  };

  return (
    <div className="min-h-screen bg-gray-50 py-12">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="text-center mb-12">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
          >
            <h1 className="text-4xl font-bold text-gray-900 mb-4">Find Your Perfect Plan</h1>
            <p className="text-xl text-gray-600 max-w-3xl mx-auto">
              Tell us about yourself and we'll match you with the best insurance plans tailored to your needs.
            </p>
          </motion.div>
        </div>

        <div className="grid lg:grid-cols-3 gap-8">
          {/* Form Section */}
          <motion.div
            initial={{ opacity: 0, x: -30 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.6 }}
            className="lg:col-span-1"
          >
            <div className="card sticky top-24">
              <div className="flex items-center mb-6">
                <Search className="h-6 w-6 text-primary-600 mr-2" />
                <h2 className="text-2xl font-semibold">Search Criteria</h2>
              </div>

              <form onSubmit={handleSubmit} className="space-y-6">
                {/* Age Group */}
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    Age Group
                  </label>
                  <select
                    value={formData.ageGroup}
                    onChange={(e) => handleInputChange('ageGroup', e.target.value)}
                    className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent"
                    required
                  >
                    <option value="">Select age group</option>
                    {ageGroups.map(group => (
                      <option key={group} value={group}>{group}</option>
                    ))}
                  </select>
                </div>

                {/* Tobacco Use */}
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    Do you use tobacco?
                  </label>
                  <div className="space-y-2">
                    {["No", "Yes", "Prefer not to say"].map(option => (
                      <label key={option} className="flex items-center">
                        <input
                          type="radio"
                          name="tobacco"
                          value={option}
                          checked={formData.tobacco === option}
                          onChange={(e) => handleInputChange('tobacco', e.target.value)}
                          className="mr-2"
                          required
                        />
                        {option}
                      </label>
                    ))}
                  </div>
                </div>

                {/* Plan Type */}
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    Type of Insurance
                  </label>
                  <select
                    value={formData.planType}
                    onChange={(e) => handleInputChange('planType', e.target.value)}
                    className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent"
                    required
                  >
                    <option value="">Select plan type</option>
                    {planTypes.map(type => (
                      <option key={type} value={type}>{type}</option>
                    ))}
                  </select>
                </div>

                {/* State */}
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    State (optional)
                  </label>
                  <select
                    value={formData.state}
                    onChange={(e) => handleInputChange('state', e.target.value)}
                    className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent"
                  >
                    <option value="">Any state</option>
                    {states.slice(1).map(state => (
                      <option key={state} value={state}>{state}</option>
                    ))}
                  </select>
                </div>

                {/* Coverage Preferences */}
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    Coverage Preferences (optional)
                  </label>
                  <div className="space-y-2">
                    {coverageNeeds.map(need => (
                      <label key={need} className="flex items-center">
                        <input
                          type="checkbox"
                          checked={formData.needs.includes(need)}
                          onChange={() => handleNeedsChange(need)}
                          className="mr-2"
                        />
                        {need}
                      </label>
                    ))}
                  </div>
                </div>

                {/* Submit Button */}
                <button
                  type="submit"
                  disabled={isLoading}
                  className="w-full btn-primary flex items-center justify-center"
                >
                  {isLoading ? (
                    <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-white"></div>
                  ) : (
                    <>
                      <Search className="h-4 w-4 mr-2" />
                      Find Matching Plans
                    </>
                  )}
                </button>
              </form>
            </div>
          </motion.div>

          {/* Results Section */}
          <motion.div
            initial={{ opacity: 0, x: 30 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.6, delay: 0.2 }}
            className="lg:col-span-2"
          >
            {!results ? (
              <div className="card text-center py-12">
                <Shield className="h-16 w-16 text-gray-400 mx-auto mb-4" />
                <h3 className="text-xl font-semibold text-gray-900 mb-2">Ready to find your plan?</h3>
                <p className="text-gray-600">
                  Fill out the form on the left to get personalized plan recommendations.
                </p>
              </div>
            ) : (
              <div className="space-y-6">
                <div className="flex items-center justify-between">
                  <h2 className="text-2xl font-semibold text-gray-900">
                    Top Matching Plans ({results.length})
                  </h2>
                  <div className="flex items-center space-x-2 text-sm text-gray-600">
                    <Filter className="h-4 w-4" />
                    <span>Sorted by match score</span>
                  </div>
                </div>

                {results.map((plan, index) => (
                  <motion.div
                    key={index}
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.6, delay: index * 0.1 }}
                    className="card hover:shadow-xl transition-shadow"
                  >
                    <div className="flex justify-between items-start mb-4">
                      <div>
                        <h3 className="text-xl font-semibold text-gray-900 mb-2">
                          {plan.name}
                        </h3>
                        <div className="flex items-center space-x-4 text-sm text-gray-600">
                          <span className="flex items-center">
                            <Shield className="h-4 w-4 mr-1" />
                            {plan.metalLevel} Level
                          </span>
                          <span className="flex items-center">
                            <Users className="h-4 w-4 mr-1" />
                            {plan.planType}
                          </span>
                        </div>
                      </div>
                      <div className="text-right">
                        <div className="text-2xl font-bold text-primary-600">
                          ₹{plan.cost}
                        </div>
                        <div className="text-sm text-gray-500">per month</div>
                      </div>
                    </div>

                    <div className="grid md:grid-cols-2 gap-4 mb-4">
                      <div className="space-y-2">
                        <div className="flex items-center text-sm">
                          <Heart className="h-4 w-4 mr-2 text-green-500" />
                          Wellness: {plan.wellness}
                        </div>
                        <div className="flex items-center text-sm">
                          <Users className="h-4 w-4 mr-2 text-blue-500" />
                          Maternity: {plan.maternity}
                        </div>
                      </div>
                      <div className="space-y-2">
                        <div className="flex items-center text-sm">
                          <Shield className="h-4 w-4 mr-2 text-purple-500" />
                          Mental Health: {plan.mentalHealth}
                        </div>
                        <div className="flex items-center text-sm">
                          <CheckCircle className="h-4 w-4 mr-2 text-green-500" />
                          Match Score: {plan.matchScore}/4
                        </div>
                      </div>
                    </div>

                    <div className="flex space-x-3">
                      <button className="btn-primary flex-1">
                        View Details
                        <ArrowRight className="h-4 w-4 ml-2" />
                      </button>
                      <button className="btn-secondary flex-1">
                        <Calculator className="h-4 w-4 mr-2" />
                        Compare
                      </button>
                    </div>
                  </motion.div>
                ))}
              </div>
            )}
          </motion.div>
        </div>
      </div>
    </div>
  );
};

export default PlanFinder; 