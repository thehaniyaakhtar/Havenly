import React from 'react';
import { motion } from 'framer-motion';
import { 
  Shield, 
  Heart, 
  Users, 
  Award, 
  Target, 
  CheckCircle,
  Phone,
  Mail,
  MapPin,
  Clock,
  Star
} from 'lucide-react';

const About = () => {
  const values = [
    {
      icon: <Shield className="h-8 w-8" />,
      title: "Trust & Security",
      description: "Your data and privacy are our top priorities. We use bank-level security to protect your information."
    },
    {
      icon: <Heart className="h-8 w-8" />,
      title: "Health First",
      description: "We believe everyone deserves access to quality healthcare that fits their lifestyle and budget."
    },
    {
      icon: <Users className="h-8 w-8" />,
      title: "Community Focus",
      description: "Building a community of informed healthcare consumers who support each other's wellness journey."
    },
    {
      icon: <Target className="h-8 w-8" />,
      title: "Personalized Care",
      description: "Every recommendation is tailored to your unique needs, preferences, and life circumstances."
    }
  ];

  const team = [
    {
      name: "Dr. Sarah Chen",
      role: "Chief Medical Officer",
      bio: "Board-certified physician with 15+ years in healthcare policy and patient advocacy.",
      image: "https://images.unsplash.com/photo-1559839734-2b71ea197ec2?w=150&h=150&fit=crop&crop=face"
    },
    {
      name: "Michael Rodriguez",
      role: "Head of AI & Technology",
      bio: "Former Google AI researcher specializing in healthcare machine learning and predictive analytics.",
      image: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150&h=150&fit=crop&crop=face"
    },
    {
      name: "Emily Johnson",
      role: "VP of Customer Experience",
      bio: "Healthcare industry veteran focused on making insurance accessible and understandable for everyone.",
      image: "https://images.unsplash.com/photo-1494790108755-2616b612b786?w=150&h=150&fit=crop&crop=face"
    }
  ];

  const milestones = [
    {
      year: "2024",
      title: "AI-Powered Platform Launch",
      description: "Launched our revolutionary AI insurance advisor platform"
    },
    {
      year: "2023",
      title: "Series A Funding",
      description: "Secured $10M in funding to expand our technology and team"
    },
    {
      year: "2022",
      title: "Company Founded",
      description: "Founded with a mission to democratize healthcare access"
    }
  ];

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Hero Section */}
      <section className="bg-white py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
            className="text-center"
          >
            <h1 className="text-5xl font-bold text-gray-900 mb-6">
              About <span className="text-gradient">Havenly</span>
            </h1>
            <p className="text-xl text-gray-600 max-w-3xl mx-auto mb-8">
              We're on a mission to make healthcare insurance simple, transparent, and accessible for everyone. 
              Our AI-powered platform helps you find the perfect coverage that fits your life and budget.
            </p>
            <div className="flex items-center justify-center space-x-8 text-sm text-gray-500">
              <div className="flex items-center">
                <Clock className="h-4 w-4 mr-2" />
                Founded 2022
              </div>
              <div className="flex items-center">
                <Users className="h-4 w-4 mr-2" />
                50,000+ Customers
              </div>
              <div className="flex items-center">
                <Award className="h-4 w-4 mr-2" />
                Industry Leader
              </div>
            </div>
          </motion.div>
        </div>
      </section>

      {/* Mission Section */}
      <section className="py-20 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid lg:grid-cols-2 gap-12 items-center">
            <motion.div
              initial={{ opacity: 0, x: -30 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ duration: 0.8 }}
            >
              <h2 className="text-4xl font-bold text-gray-900 mb-6">Our Mission</h2>
              <p className="text-lg text-gray-600 mb-6">
                Healthcare insurance shouldn't be complicated. We believe everyone deserves access to quality 
                coverage that they can understand and afford. That's why we built Havenly - to bridge the gap 
                between complex insurance policies and real people who need protection.
              </p>
              <p className="text-lg text-gray-600 mb-8">
                Using cutting-edge AI technology, we analyze thousands of plans to find the perfect match for 
                your unique situation. No more guesswork, no more confusion - just clear, personalized recommendations 
                that put your health first.
              </p>
              <div className="flex items-center space-x-4">
                <div className="flex items-center">
                  <CheckCircle className="h-5 w-5 text-green-500 mr-2" />
                  <span className="text-sm font-medium">AI-Powered Matching</span>
                </div>
                <div className="flex items-center">
                  <CheckCircle className="h-5 w-5 text-green-500 mr-2" />
                  <span className="text-sm font-medium">Transparent Pricing</span>
                </div>
              </div>
            </motion.div>
            <motion.div
              initial={{ opacity: 0, x: 30 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ duration: 0.8, delay: 0.2 }}
              className="relative"
            >
              <div className="bg-gradient-to-br from-primary-500 to-secondary-500 rounded-2xl p-8 text-white">
                <Shield className="h-16 w-16 mb-6" />
                <h3 className="text-2xl font-bold mb-4">Why Choose Havenly?</h3>
                <ul className="space-y-3">
                  <li className="flex items-center">
                    <CheckCircle className="h-5 w-5 mr-3" />
                    Personalized AI recommendations
                  </li>
                  <li className="flex items-center">
                    <CheckCircle className="h-5 w-5 mr-3" />
                    Side-by-side plan comparisons
                  </li>
                  <li className="flex items-center">
                    <CheckCircle className="h-5 w-5 mr-3" />
                    Real-time cost analysis
                  </li>
                  <li className="flex items-center">
                    <CheckCircle className="h-5 w-5 mr-3" />
                    24/7 expert support
                  </li>
                </ul>
              </div>
            </motion.div>
          </div>
        </div>
      </section>

      {/* Values Section */}
      <section className="py-20 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
            className="text-center mb-16"
          >
            <h2 className="text-4xl font-bold text-gray-900 mb-4">Our Values</h2>
            <p className="text-xl text-gray-600 max-w-3xl mx-auto">
              These core principles guide everything we do and every decision we make.
            </p>
          </motion.div>
          
          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
            {values.map((value, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 30 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.6, delay: index * 0.1 }}
                className="card text-center group hover:scale-105"
              >
                <div className="text-primary-600 mb-4 group-hover:scale-110 transition-transform">
                  {value.icon}
                </div>
                <h3 className="text-xl font-semibold mb-3">{value.title}</h3>
                <p className="text-gray-600">{value.description}</p>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Team Section */}
      <section className="py-20 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
            className="text-center mb-16"
          >
            <h2 className="text-4xl font-bold text-gray-900 mb-4">Meet Our Team</h2>
            <p className="text-xl text-gray-600 max-w-3xl mx-auto">
              The passionate experts behind Havenly's mission to transform healthcare insurance.
            </p>
          </motion.div>
          
          <div className="grid md:grid-cols-3 gap-8">
            {team.map((member, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 30 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.6, delay: index * 0.2 }}
                className="card text-center"
              >
                <img
                  src={member.image}
                  alt={member.name}
                  className="w-24 h-24 rounded-full mx-auto mb-4 object-cover"
                />
                <h3 className="text-xl font-semibold mb-2">{member.name}</h3>
                <p className="text-primary-600 font-medium mb-3">{member.role}</p>
                <p className="text-gray-600 text-sm">{member.bio}</p>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Milestones Section */}
      <section className="py-20 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
            className="text-center mb-16"
          >
            <h2 className="text-4xl font-bold text-gray-900 mb-4">Our Journey</h2>
            <p className="text-xl text-gray-600">
              Key milestones in our mission to democratize healthcare access.
            </p>
          </motion.div>
          
          <div className="grid md:grid-cols-3 gap-8">
            {milestones.map((milestone, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 30 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.6, delay: index * 0.2 }}
                className="card text-center"
              >
                <div className="text-3xl font-bold text-primary-600 mb-4">{milestone.year}</div>
                <h3 className="text-xl font-semibold mb-3">{milestone.title}</h3>
                <p className="text-gray-600">{milestone.description}</p>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Contact Section */}
      <section className="py-20 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
            className="text-center mb-16"
          >
            <h2 className="text-4xl font-bold text-gray-900 mb-4">Get in Touch</h2>
            <p className="text-xl text-gray-600">
              Have questions? We'd love to hear from you.
            </p>
          </motion.div>
          
          <div className="grid md:grid-cols-3 gap-8">
            <motion.div
              initial={{ opacity: 0, y: 30 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6 }}
              className="card text-center"
            >
              <Phone className="h-8 w-8 text-primary-600 mx-auto mb-4" />
              <h3 className="text-lg font-semibold mb-2">Call Us</h3>
              <p className="text-gray-600">1-800-HAVENLY</p>
              <p className="text-sm text-gray-500">Mon-Fri 9AM-6PM EST</p>
            </motion.div>
            
            <motion.div
              initial={{ opacity: 0, y: 30 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: 0.1 }}
              className="card text-center"
            >
              <Mail className="h-8 w-8 text-primary-600 mx-auto mb-4" />
              <h3 className="text-lg font-semibold mb-2">Email Us</h3>
              <p className="text-gray-600">hello@havenly.com</p>
              <p className="text-sm text-gray-500">We'll respond within 24 hours</p>
            </motion.div>
            
            <motion.div
              initial={{ opacity: 0, y: 30 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: 0.2 }}
              className="card text-center"
            >
              <MapPin className="h-8 w-8 text-primary-600 mx-auto mb-4" />
              <h3 className="text-lg font-semibold mb-2">Visit Us</h3>
              <p className="text-gray-600">San Francisco, CA</p>
              <p className="text-sm text-gray-500">Innovation District</p>
            </motion.div>
          </div>
        </div>
      </section>
    </div>
  );
};

export default About; 