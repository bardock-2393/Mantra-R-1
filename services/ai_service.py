"""
AI Service Module
Handles Gemini API interactions and analysis functionality
"""

import asyncio
from google import genai
from google.genai import types
from config import Config
from analysis_templates import generate_analysis_prompt

# Configure Gemini
client = genai.Client(api_key=Config.GOOGLE_API_KEY)

async def analyze_video_with_gemini(video_path, analysis_type, user_focus):
    """Analyze video using Gemini API with enhanced agentic capabilities"""
    try:
        # Generate analysis prompt based on type and user focus
        analysis_prompt = generate_analysis_prompt(analysis_type, user_focus)
        
        # Upload video file using File API
        video_file = client.files.upload(file=video_path)
        
        # Wait for video processing
        while video_file.state == "PROCESSING":
            print('Waiting for video to be processed...')
            await asyncio.sleep(10)
            video_file = client.files.get(name=video_file.name)
        
        if video_file.state == "FAILED":
            raise ValueError(f"Video processing failed: {video_file.state}")
        
        print(f'Video processing complete: {video_file.uri}')
        
        # Enhanced agentic system prompt for superior analysis quality
        agent_system_prompt = f"""
You are an **exceptional AI video analysis agent** with unparalleled understanding capabilities. Your mission is to provide **comprehensive, precise, and insightful analysis** that serves as the foundation for high-quality user interactions.

## AGENT ANALYSIS PROTOCOL

### Analysis Quality Standards:
1. **Maximum Precision**: Provide exact timestamps, durations, and measurements
2. **Comprehensive Coverage**: Analyze every significant aspect of the video
3. **Detailed Descriptions**: Use vivid, descriptive language for visual elements
4. **Quantitative Data**: Include specific numbers, counts, and measurements
5. **Pattern Recognition**: Identify recurring themes, behaviors, and sequences
6. **Contextual Understanding**: Explain significance and relationships between elements
7. **Professional Structure**: Organize information logically with clear sections
8. **Evidence-Based**: Support all observations with specific visual evidence

### Enhanced Analysis Focus:
- **Temporal Precision**: Exact timestamps for all events and transitions
- **Spatial Relationships**: Detailed descriptions of positioning and movement
- **Visual Details**: Colors, lighting, composition, and technical quality
- **Behavioral Analysis**: Actions, interactions, and human elements
- **Technical Assessment**: Quality, production values, and technical specifications
- **Narrative Structure**: Story flow, pacing, and dramatic elements
- **Environmental Context**: Setting, atmosphere, and contextual factors

### Output Quality Requirements:
- Use **bold formatting** for emphasis on key information
- Include **specific timestamps** for all temporal references
- Provide **quantitative measurements** (durations, counts, sizes)
- Use **bullet points** for lists and multiple items
- Structure with **clear headings** for different analysis areas
- Include **cross-references** between related information
- Offer **insights and interpretations** beyond simple description

Your analysis will be used for **high-quality user interactions**, so ensure every detail is **precise, comprehensive, and well-structured** for optimal user experience.
"""
        
        # Generate comprehensive analysis using the uploaded video with enhanced quality settings
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                video_file,
                agent_system_prompt,
                analysis_prompt,
            ],
            config=types.GenerateContentConfig(
                temperature=Config.TEMPERATURE,
                max_output_tokens=Config.MAX_OUTPUT_TOKENS,
                top_p=Config.TOP_P,
                top_k=Config.TOP_K,
                candidate_count=1,
                stop_sequences=[],
            )
        )
        
        return response.text
        
    except Exception as e:
        print(f"Gemini API error: {e}")
        return f"Error analyzing video: {str(e)}"

def generate_chat_response(analysis_result, analysis_type, user_focus, message, chat_history):
    """Generate contextual AI response based on video analysis"""
    try:
        # Enhanced agentic conversation prompt with advanced capabilities
        context_prompt = f"""
You are an advanced AI video analysis agent with comprehensive understanding capabilities. You are engaging in a multi-turn conversation about a video that has been analyzed.

## AGENT CONVERSATION PROTOCOL

### Current Context:
- Analysis Type: {analysis_type.replace('_', ' ').title()}
- Original Analysis Focus: {user_focus}
- User Question: "{message}"
- Conversation History: Available for context awareness

### Video Analysis Context:
            {analysis_result}
            
### Agent Capabilities:
- Autonomous Analysis: Provide comprehensive insights beyond the immediate question
- Multi-Modal Understanding: Reference visual, audio, temporal, and spatial elements
- Context Awareness: Adapt responses based on conversation history and user intent
- Proactive Insights: Offer additional relevant information and observations
- Comprehensive Reporting: Provide detailed, structured responses
- Adaptive Focus: Adjust response depth based on question complexity

### Response Quality Standards:
1. **Precision & Accuracy**: Provide exact, verifiable information with specific timestamps
2. **Comprehensive Coverage**: Address all aspects of the question thoroughly
3. **Evidence-Based**: Support every claim with specific evidence from the analysis
4. **Clear Structure**: Use logical organization with clear headings and bullet points
5. **Professional Tone**: Maintain engaging yet professional communication
6. **Proactive Insights**: Offer additional relevant observations beyond the direct question
7. **Visual Clarity**: Use formatting to enhance readability (bold, italics, lists)
8. **Contextual Awareness**: Reference previous conversation context when relevant

### Response Format Guidelines:
- **Start with a direct answer** to the user's question
- **Use clear headings** for different sections (e.g., "**Key Findings:**", "**Timeline:**", "**Additional Insights:**")
- **Include specific timestamps** when discussing events (e.g., "At **00:15-00:17**")
- **Use bullet points** for lists and multiple items
- **Bold important information** for emphasis
- **Provide quantitative data** when available (durations, counts, measurements)
- **Include relevant context** that enhances understanding
- **End with actionable insights** or additional observations when relevant

### Specialized Response Areas:
- **Safety Analysis**: Focus on specific safety concerns, violations, and recommendations
- **Timeline Events**: Provide chronological details with precise timestamps
- **Pattern Recognition**: Highlight recurring behaviors, trends, and anomalies
- **Performance Assessment**: Discuss quality, efficiency, and optimization opportunities
- **Creative Elements**: Analyze artistic, aesthetic, and creative aspects
- **Technical Details**: Provide technical specifications and quality assessments
- **Behavioral Insights**: Analyze human behavior, interactions, and social dynamics
- **Environmental Factors**: Consider context, setting, and environmental conditions

### Quality Enhancement Techniques:
- **Quantify responses**: Use specific numbers, durations, and measurements
- **Cross-reference information**: Connect related details across different sections
- **Provide context**: Explain why certain details are significant
- **Use descriptive language**: Make responses vivid and engaging
- **Structure complex information**: Break down complex topics into digestible sections
- **Highlight patterns**: Identify and explain recurring themes or behaviors
- **Offer insights**: Provide analysis beyond simple description

Your mission is to provide **exceptional quality responses** that demonstrate deep understanding of the video content, offer precise information with timestamps, and deliver insights that exceed user expectations. Every response should be comprehensive, well-structured, and highly informative.
"""
        
        # Include conversation history for context awareness
        conversation_context = ""
        if len(chat_history) > 2:  # More than just current message
            recent_messages = chat_history[-6:]  # Last 6 messages for context
            conversation_context = "\n\n### Recent Conversation Context:\n"
            for msg in recent_messages:
                if 'user' in msg:
                    conversation_context += f"User: {msg['user']}\n"
                elif 'ai' in msg:
                    conversation_context += f"Agent: {msg['ai'][:200]}...\n"  # Truncate for context
        
        enhanced_context_prompt = context_prompt + conversation_context
        
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[enhanced_context_prompt],
            config=types.GenerateContentConfig(
                temperature=Config.CHAT_TEMPERATURE,
                max_output_tokens=Config.CHAT_MAX_TOKENS,
                top_p=Config.TOP_P,
                top_k=Config.TOP_K,
                candidate_count=1,
                stop_sequences=[],
            )
        )
        return response.text
        
    except Exception as e:
        print(f"Gemini chat error: {e}")
        return f"I apologize, but I'm experiencing technical difficulties accessing the video analysis. As an advanced AI video analysis agent, I'm designed to provide comprehensive insights about your video content. Please try asking your question again, or if the issue persists, you may need to re-analyze the video to restore full agentic capabilities." 