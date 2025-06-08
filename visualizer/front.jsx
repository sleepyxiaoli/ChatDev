import React, { useState, useEffect, useRef } from 'react';
import { Send, Users, MessageCircle, Info, Play, RotateCcw, Settings } from 'lucide-react';

export default function ChatDevInterface() {
  const [messages, setMessages] = useState([]);
  const [newMessage, setNewMessage] = useState('');
  const [selectedRole, setSelectedRole] = useState('产品经理');
  const [isLoading, setIsLoading] = useState(false);
  const [showGuide, setShowGuide] = useState(true);
  const messagesEndRef = useRef(null);

  const roles = [
    '产品经理', 'UI设计师', '前端开发', '后端开发', 
    '测试工程师', '项目经理', '系统架构师', '用户体验师'
  ];

  const roleColors = {
    '产品经理': 'bg-blue-500',
    'UI设计师': 'bg-purple-500',
    '前端开发': 'bg-green-500',
    '后端开发': 'bg-red-500',
    '测试工程师': 'bg-yellow-500',
    '项目经理': 'bg-indigo-500',
    '系统架构师': 'bg-gray-500',
    '用户体验师': 'bg-pink-500'
  };

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    fetchMessages();
  }, []);

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const fetchMessages = async () => {
    try {
      const response = await fetch('/get_messages');
      const data = await response.json();
      setMessages(data);
    } catch (error) {
      console.error('获取消息失败:', error);
    }
  };

  const sendMessage = async () => {
    if (!newMessage.trim() || !selectedRole) return;

    setIsLoading(true);
    try {
      const response = await fetch('/send_message', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          role: selectedRole,
          text: newMessage.trim()
        })
      });

      if (response.ok) {
        setNewMessage('');
        await fetchMessages();
      }
    } catch (error) {
      console.error('发送消息失败:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  const clearMessages = () => {
    setMessages([]);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900">
      {/* Header */}
      <div className="bg-black/20 backdrop-blur-sm border-b border-white/10">
        <div className="max-w-7xl mx-auto px-4 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-3">
              <div className="w-10 h-10 bg-gradient-to-r from-blue-500 to-purple-600 rounded-lg flex items-center justify-center">
                <MessageCircle className="w-6 h-6 text-white" />
              </div>
              <div>
                <h1 className="text-2xl font-bold text-white">ChatDev 协作平台</h1>
                <p className="text-sm text-gray-300">多角色智能开发助手</p>
              </div>
            </div>
            <div className="flex items-center space-x-2">
              <button
                onClick={() => setShowGuide(!showGuide)}
                className="px-4 py-2 bg-white/10 text-white rounded-lg hover:bg-white/20 transition-colors flex items-center space-x-2"
              >
                <Info className="w-4 h-4" />
                <span>使用指南</span>
              </button>
              <button
                onClick={clearMessages}
                className="px-4 py-2 bg-red-500/20 text-red-300 rounded-lg hover:bg-red-500/30 transition-colors flex items-center space-x-2"
              >
                <RotateCcw className="w-4 h-4" />
                <span>清空对话</span>
              </button>
            </div>
          </div>
        </div>
      </div>

      <div className="max-w-7xl mx-auto px-4 py-6">
        <div className="grid grid-cols-12 gap-6 h-full">
          {/* Sidebar */}
          <div className="col-span-3">
            {/* Role Selection */}
            <div className="bg-white/5 backdrop-blur-sm rounded-xl p-6 border border-white/10 mb-6">
              <h3 className="text-lg font-semibold text-white mb-4 flex items-center">
                <Users className="w-5 h-5 mr-2" />
                选择角色
              </h3>
              <div className="space-y-2">
                {roles.map((role) => (
                  <button
                    key={role}
                    onClick={() => setSelectedRole(role)}
                    className={`w-full text-left px-3 py-2 rounded-lg transition-colors flex items-center space-x-3 ${
                      selectedRole === role
                        ? 'bg-blue-500/30 text-blue-200 border border-blue-400/50'
                        : 'text-gray-300 hover:bg-white/10'
                    }`}
                  >
                    <div className={`w-3 h-3 rounded-full ${roleColors[role]}`}></div>
                    <span>{role}</span>
                  </button>
                ))}
              </div>
            </div>

            {/* Statistics */}
            <div className="bg-white/5 backdrop-blur-sm rounded-xl p-6 border border-white/10">
              <h3 className="text-lg font-semibold text-white mb-4">项目状态</h3>
              <div className="space-y-3">
                <div className="flex justify-between">
                  <span className="text-gray-300">总消息数</span>
                  <span className="text-white font-medium">{messages.length}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-gray-300">活跃角色</span>
                  <span className="text-white font-medium">
                    {new Set(messages.map(m => m.role)).size}
                  </span>
                </div>
                <div className="flex justify-between">
                  <span className="text-gray-300">项目进度</span>
                  <span className="text-green-400 font-medium">进行中</span>
                </div>
              </div>
            </div>
          </div>

          {/* Main Chat Area */}
          <div className="col-span-9">
            <div className="bg-white/5 backdrop-blur-sm rounded-xl border border-white/10 flex flex-col h-screen max-h-[calc(100vh-200px)]">
              {/* Chat Header */}
              <div className="px-6 py-4 border-b border-white/10">
                <div className="flex items-center justify-between">
                  <h2 className="text-xl font-semibold text-white">开发讨论区</h2>
                  <div className="flex items-center space-x-2 text-sm text-gray-300">
                    <div className="w-2 h-2 bg-green-500 rounded-full animate-pulse"></div>
                    <span>实时同步</span>
                  </div>
                </div>
              </div>

              {/* Messages */}
              <div className="flex-1 overflow-y-auto p-6 space-y-4">
                {messages.length === 0 ? (
                  <div className="text-center py-12">
                    <MessageCircle className="w-16 h-16 text-gray-500 mx-auto mb-4" />
                    <p className="text-gray-400 text-lg">还没有消息，开始你的第一次对话吧！</p>
                  </div>
                ) : (
                  messages.map((message, index) => (
                    <div key={index} className="flex space-x-4">
                      <div className={`w-10 h-10 rounded-full ${roleColors[message.role] || 'bg-gray-500'} flex items-center justify-center text-white font-medium text-sm flex-shrink-0`}>
                        {message.role.slice(0, 2)}
                      </div>
                      <div className="flex-1 min-w-0">
                        <div className="flex items-center space-x-2 mb-1">
                          <span className="font-medium text-white">{message.role}</span>
                          <span className="text-xs text-gray-400">刚刚</span>
                        </div>
                        <div className="bg-white/10 rounded-lg p-3 text-gray-200 whitespace-pre-wrap">
                          {message.text}
                        </div>
                      </div>
                    </div>
                  ))
                )}
                <div ref={messagesEndRef} />
              </div>

              {/* Message Input */}
              <div className="p-6 border-t border-white/10">
                <div className="flex space-x-4">
                  <div className="flex-1">
                    <div className="flex items-center space-x-2 mb-2">
                      <div className={`w-4 h-4 rounded-full ${roleColors[selectedRole]}`}></div>
                      <span className="text-sm font-medium text-gray-300">以 {selectedRole} 身份发言</span>
                    </div>
                    <div className="flex space-x-3">
                      <textarea
                        value={newMessage}
                        onChange={(e) => setNewMessage(e.target.value)}
                        onKeyPress={handleKeyPress}
                        placeholder="输入你的想法..."
                        className="flex-1 bg-white/10 border border-white/20 rounded-lg px-4 py-3 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none"
                        rows="3"
                      />
                      <button
                        onClick={sendMessage}
                        disabled={!newMessage.trim() || isLoading}
                        className="px-6 py-3 bg-gradient-to-r from-blue-500 to-purple-600 text-white rounded-lg hover:from-blue-600 hover:to-purple-700 disabled:opacity-50 disabled:cursor-not-allowed transition-all flex items-center space-x-2 self-end"
                      >
                        <Send className="w-4 h-4" />
                        <span>{isLoading ? '发送中...' : '发送'}</span>
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Usage Guide Modal */}
      {showGuide && (
        <div className="fixed inset-0 bg-black/50 backdrop-blur-sm flex items-center justify-center p-4 z-50">
          <div className="bg-slate-800 rounded-xl p-8 max-w-2xl w-full max-h-[80vh] overflow-y-auto border border-white/20">
            <div className="flex items-center justify-between mb-6">
              <h2 className="text-2xl font-bold text-white">使用指南</h2>
              <button
                onClick={() => setShowGuide(false)}
                className="text-gray-400 hover:text-white transition-colors text-2xl"
              >
                ×
              </button>
            </div>
            
            <div className="space-y-6 text-gray-300">
              <div>
                <h3 className="text-lg font-semibold text-white mb-3">🚀 快速开始</h3>
                <p className="mb-3">欢迎使用ChatDev协作平台！这是一个模拟多角色软件开发团队的智能助手。</p>
                <div className="bg-slate-700 rounded-lg p-4">
                  <p><strong>1.</strong> 在左侧选择角色（产品经理、开发者、设计师等）</p>
                  <p><strong>2.</strong> 在下方输入框中输入消息</p>
                  <p><strong>3.</strong> 点击发送或按回车键发送消息</p>
                  <p><strong>4.</strong> 查看团队成员之间的协作对话</p>
                </div>
              </div>

              <div>
                <h3 className="text-lg font-semibold text-white mb-3">👥 角色说明</h3>
                <div className="grid grid-cols-2 gap-3">
                  {roles.map((role) => (
                    <div key={role} className="flex items-center space-x-2 p-2 bg-slate-700 rounded">
                      <div className={`w-3 h-3 rounded-full ${roleColors[role]}`}></div>
                      <span>{role}</span>
                    </div>
                  ))}
                </div>
              </div>

              <div>
                <h3 className="text-lg font-semibold text-white mb-3">💡 使用技巧</h3>
                <div className="bg-slate-700 rounded-lg p-4 space-y-2">
                  <p>• 切换不同角色来模拟团队讨论</p>
                  <p>• 使用产品经理角色来定义需求</p>
                  <p>• 使用开发者角色来讨论技术实现</p>
                  <p>• 使用设计师角色来讨论界面和交互</p>
                  <p>• 查看右侧统计信息了解项目状态</p>
                </div>
              </div>

              <div>
                <h3 className="text-lg font-semibold text-white mb-3">🔧 API集成</h3>
                <div className="bg-slate-700 rounded-lg p-4">
                  <p>本前端已集成你的Flask后端API：</p>
                  <p>• <code className="bg-slate-600 px-2 py-1 rounded">GET /get_messages</code> - 获取消息</p>
                  <p>• <code className="bg-slate-600 px-2 py-1 rounded">POST /send_message</code> - 发送消息</p>
                </div>
              </div>
            </div>

            <div className="mt-8">
              <button
                onClick={() => setShowGuide(false)}
                className="w-full py-3 bg-gradient-to-r from-blue-500 to-purple-600 text-white rounded-lg hover:from-blue-600 hover:to-purple-700 transition-all"
              >
                开始使用
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}