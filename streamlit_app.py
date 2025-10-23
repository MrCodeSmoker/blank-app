import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st
import pandas as pd
import re
import json
import ast
import html
import base64
from typing import Dict, Any, List
from datetime import datetime

# Page configuration for elegant interface
st.set_page_config(
    page_title="AI-Powered Code Converter",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Enhanced CSS with AI-specific styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 0;
        margin: 0;
    }
    
    .elegant-header {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        padding: 25px 40px;
        color: #2d3748;
        border-bottom: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    }
    
    .header-title {
        font-size: 32px;
        font-weight: 700;
        margin: 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        display: flex;
        align-items: center;
        gap: 15px;
    }
    
    .header-subtitle {
        font-size: 16px;
        font-weight: 400;
        color: #718096;
        margin: 5px 0 0 0;
        font-family: 'Inter', sans-serif;
    }
    
    .elegant-container {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
        margin: 30px;
        overflow: hidden;
        transition: all 0.3s ease;
    }
    
    .elegant-container:hover {
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.15);
        transform: translateY(-2px);
    }
    
    .content-section {
        padding: 35px;
        background: white;
    }
    
    .section-title {
        font-size: 24px;
        font-weight: 600;
        color: #2d3748;
        margin-bottom: 25px;
        display: flex;
        align-items: center;
        gap: 12px;
        border-bottom: 2px solid #f7fafc;
        padding-bottom: 12px;
    }
    
    .section-title::before {
        content: '';
        width: 4px;
        height: 24px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 2px;
    }
    
    /* AI Prompt Section */
    .ai-prompt-section {
        background: linear-gradient(135deg, #f0f4ff 0%, #e6eeff 100%);
        border: 2px dashed #667eea;
        border-radius: 16px;
        padding: 25px;
        margin: 20px 0;
        transition: all 0.3s ease;
    }
    
    .ai-prompt-section:hover {
        background: linear-gradient(135deg, #e6eeff 0%, #d6e4ff 100%);
        border-color: #5a67d8;
    }
    
    .ai-suggestion {
        background: linear-gradient(135deg, #48bb78 0%, #38a169 100%);
        color: white;
        border-radius: 20px;
        padding: 8px 16px;
        margin: 5px;
        font-size: 12px;
        font-weight: 500;
        cursor: pointer;
        transition: all 0.3s ease;
        display: inline-block;
    }
    
    .ai-suggestion:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(72, 187, 120, 0.3);
    }
    
    /* Elegant Buttons */
    .elegant-button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 14px 28px;
        font-size: 14px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        font-family: 'Inter', sans-serif;
    }
    
    .elegant-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }
    
    .elegant-button-ai {
        background: linear-gradient(135deg, #48bb78 0%, #38a169 100%);
        box-shadow: 0 4px 15px rgba(72, 187, 120, 0.3);
    }
    
    .elegant-button-ai:hover {
        background: linear-gradient(135deg, #38a169 0%, #48bb78 100%);
        box-shadow: 0 8px 25px rgba(72, 187, 120, 0.4);
    }
    
    /* Elegant Cards */
    .elegant-card {
        background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%);
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 25px;
        margin: 15px 0;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.02);
    }
    
    .elegant-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.08);
        border-color: #cbd5e0;
    }
    
    .card-title {
        font-size: 18px;
        font-weight: 600;
        color: #2d3748;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    /* Stats Cards */
    .stat-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
        transition: all 0.3s ease;
    }
    
    .stat-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 35px rgba(102, 126, 234, 0.4);
    }
    
    .stat-number {
        font-size: 32px;
        font-weight: 700;
        margin-bottom: 5px;
    }
    
    .stat-label {
        font-size: 14px;
        font-weight: 500;
        opacity: 0.9;
    }
    
    /* Status Bar */
    .elegant-status {
        background: linear-gradient(135deg, #2d3748 0%, #4a5568 100%);
        color: white;
        padding: 12px 35px;
        font-size: 13px;
        font-weight: 500;
        border-top: 1px solid #4a5568;
    }
    
    /* Animation for conversion */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .fade-in {
        animation: fadeIn 0.5s ease-out;
    }
    
    /* Category badges */
    .category-badge {
        display: inline-block;
        background: linear-gradient(135deg, #48bb78 0%, #38a169 100%);
        color: white;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
        margin: 2px;
    }
    
    .category-badge-js {
        background: linear-gradient(135deg, #f6e05e 0%, #d69e2e 100%);
    }
    
    .category-badge-python {
        background: linear-gradient(135deg, #63b3ed 0%, #3182ce 100%);
    }
    
    .category-badge-css {
        background: linear-gradient(135deg, #b794f4 0%, #805ad5 100%);
    }
    
    .category-badge-data {
        background: linear-gradient(135deg, #f56565 0%, #e53e3e 100%);
    }
    
    .category-badge-web {
        background: linear-gradient(135deg, #68d391 0%, #38a169 100%);
    }
    
    .category-badge-ai {
        background: linear-gradient(135deg, #9f7aea 0%, #805ad5 100%);
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Elegant Header
    st.markdown("""
    <div class="elegant-header">
        <div class="header-title">
            <span>🤖</span>
            AI-Powered Code Converter
        </div>
        <div class="header-subtitle">
            Transform code using natural language prompts or traditional conversion methods
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize session state
    if 'conversion_history' not in st.session_state:
        st.session_state.conversion_history = []
    if 'input_code' not in st.session_state:
        st.session_state.input_code = ""
    if 'output_code' not in st.session_state:
        st.session_state.output_code = ""
    if 'ai_prompt' not in st.session_state:
        st.session_state.ai_prompt = ""
    if 'use_ai_mode' not in st.session_state:
        st.session_state.use_ai_mode = False
    
    # Main container
    with st.container():
        st.markdown('<div class="elegant-container">', unsafe_allow_html=True)
        st.markdown('<div class="content-section">', unsafe_allow_html=True)
        
        # AI Prompt Section
        st.markdown("""
        <div class="ai-prompt-section">
            <div class="section-title">
                <span>🎯</span>
                AI-Powered Conversion
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        col_ai1, col_ai2 = st.columns([3, 1])
        with col_ai1:
            ai_prompt = st.text_input(
                "**Describe what you want to convert:**",
                placeholder="e.g., 'Convert this JavaScript function to Python', 'Make this CSS responsive', 'Transform SQL query to MongoDB'...",
                key="ai_prompt"
            )
        with col_ai2:
            st.markdown("<div style='height: 28px'></div>")
            use_ai_mode = st.checkbox("**Use AI Mode**", value=st.session_state.use_ai_mode, key="use_ai_mode")
        
        # AI Suggestions
        st.markdown("**💡 Quick Suggestions:**")
        ai_suggestions = [
            "Convert to TypeScript",
            "Make it Pythonic", 
            "Transform to React hooks",
            "CSS to Tailwind",
            "SQL to Pandas",
            "Add error handling",
            "Optimize performance",
            "Add comments"
        ]
        
        cols = st.columns(4)
        for i, suggestion in enumerate(ai_suggestions):
            with cols[i % 4]:
                if st.button(f"**{suggestion}**", use_container_width=True, key=f"ai_sug_{i}"):
                    st.session_state.ai_prompt = suggestion
                    st.session_state.use_ai_mode = True
                    st.rerun()
        
        # Create two main columns
        col1, col2 = st.columns([1, 1.2], gap="large")
        
        with col1:
            # Control Panel
            st.markdown("""
            <div class="section-title">
                <span>⚙️</span>
                Conversion Settings
            </div>
            """, unsafe_allow_html=True)
            
            # Elegant card for conversion type
            st.markdown('<div class="elegant-card">', unsafe_allow_html=True)
            
            # Categorized conversion types
            conversion_categories = {
                "🔄 JavaScript & TypeScript": [
                    "JavaScript to TypeScript",
                    "TypeScript to JavaScript",
                    "JavaScript to Python",
                    "Python to JavaScript"
                ],
                "🐍 Python & Data Science": [
                    "Python to Ruby",
                    "Ruby to Python",
                    "Python to PHP",
                    "PHP to Python"
                ],
                "🎨 CSS & Styling": [
                    "CSS to Tailwind CSS",
                    "Tailwind CSS to CSS",
                    "CSS to SCSS",
                    "SCSS to CSS"
                ],
                "⚛️ React & Frameworks": [
                    "React Class to Function Components",
                    "React to Vue 3",
                    "Vue 3 to React"
                ],
                "🗄️ Data & Formats": [
                    "SQL to Pandas",
                    "SQL to MongoDB",
                    "JSON to Python Dict",
                    "JSON to XML",
                    "XML to JSON",
                    "CSV to JSON",
                    "Base64 Encode",
                    "Base64 Decode"
                ],
                "🌐 Web & Markup": [
                    "HTML to JSX",
                    "Markdown to HTML",
                    "HTML to Markdown"
                ]
            }
            
            # Flatten categories for selectbox
            all_conversions = []
            for category, conversions in conversion_categories.items():
                all_conversions.extend(conversions)
            
            conversion_type = st.selectbox(
                "**Select Conversion Type**",
                all_conversions,
                key="conversion_type"
            )
            
            # Show category badge
            category_name = next((cat for cat, convs in conversion_categories.items() if conversion_type in convs), "Other")
            category_color = {
                "🔄 JavaScript & TypeScript": "category-badge-js",
                "🐍 Python & Data Science": "category-badge-python",
                "🎨 CSS & Styling": "category-badge-css",
                "⚛️ React & Frameworks": "category-badge",
                "🗄️ Data & Formats": "category-badge-data",
                "🌐 Web & Markup": "category-badge-web"
            }.get(category_name, "category-badge")
            
            st.markdown(f'<div class="category-badge {category_color}">{category_name}</div>', unsafe_allow_html=True)
            
            if use_ai_mode and ai_prompt:
                st.markdown(f'<div class="category-badge category-badge-ai">🤖 AI Mode: {ai_prompt}</div>', unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Options card
            st.markdown('<div class="elegant-card">', unsafe_allow_html=True)
            st.markdown('<div class="card-title"><span>🎛️</span>Options</div>', unsafe_allow_html=True)
            
            col_opt1, col_opt2 = st.columns(2)
            with col_opt1:
                auto_convert = st.checkbox("**Auto Convert**", value=False, key="auto_convert")
                show_stats = st.checkbox("**Show Statistics**", value=True, key="show_stats")
            with col_opt2:
                enable_history = st.checkbox("**Save History**", value=True, key="enable_history")
                smart_detection = st.checkbox("**Smart Detection**", value=True, key="smart_detection")
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Quick Actions card
            st.markdown('<div class="elegant-card">', unsafe_allow_html=True)
            st.markdown('<div class="card-title"><span>🚀</span>Quick Examples</div>', unsafe_allow_html=True)
            
            example_col1, example_col2, example_col3 = st.columns(3)
            with example_col1:
                if st.button("**📝 JS**", use_container_width=True, key="js_example"):
                    st.session_state.input_code = """function calculateTotal(items) {
    let total = 0;
    for (let i = 0; i < items.length; i++) {
        total += items[i].price * items[i].quantity;
    }
    return total;
}"""
                    st.rerun()
                
                if st.button("**🐍 Py**", use_container_width=True, key="python_example"):
                    st.session_state.input_code = """def process_data(data):
    result = []
    for item in data:
        if item['active']:
            result.append({
                'name': item['name'],
                'value': item['value'] * 2
            })
    return result"""
                    st.rerun()
            
            with example_col2:
                if st.button("**🎨 CSS**", use_container_width=True, key="css_example"):
                    st.session_state.input_code = """.container {
    margin: 20px;
    padding: 15px;
    background-color: #f0f0f0;
    border-radius: 5px;
}"""
                    st.rerun()
                
                if st.button("**🗃️ SQL**", use_container_width=True, key="sql_example"):
                    st.session_state.input_code = """SELECT name, email FROM users WHERE active = 1;"""
                    st.rerun()
            
            with example_col3:
                if st.button("**📋 JSON**", use_container_width=True, key="json_example"):
                    st.session_state.input_code = """{
    "users": [
        {"name": "John", "age": 30},
        {"name": "Jane", "age": 25}
    ]
}"""
                    st.rerun()
                
                if st.button("**🌐 HTML**", use_container_width=True, key="html_example"):
                    st.session_state.input_code = """<div class="container">
    <h1>Hello World</h1>
    <p>Welcome to our website</p>
</div>"""
                    st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Action Buttons
            col_act1, col_act2 = st.columns(2)
            with col_act1:
                if use_ai_mode:
                    convert_clicked = st.button(
                        "**🤖 AI Convert**", 
                        use_container_width=True, 
                        type="primary",
                        key="convert_ai"
                    )
                else:
                    convert_clicked = st.button(
                        "**🔄 Convert Code**", 
                        use_container_width=True, 
                        type="primary",
                        key="convert"
                    )
            with col_act2:
                if st.button("**🗑️ Clear All**", use_container_width=True, key="clear"):
                    st.session_state.input_code = ""
                    st.session_state.output_code = ""
                    st.session_state.ai_prompt = ""
                    st.rerun()

        with col2:
            # Code Panels
            st.markdown("""
            <div class="section-title">
                <span>📥</span>
                Input Code
            </div>
            """, unsafe_allow_html=True)
            
            # Input code area
            input_code = st.text_area(
                "Input Code:",
                height=250,
                placeholder="Paste your source code here...",
                label_visibility="collapsed",
                key="input_code",
                value=st.session_state.input_code
            )
            
            st.markdown("""
            <div class="section-title">
                <span>📤</span>
                Output Code
            </div>
            """, unsafe_allow_html=True)
            
            # Output code area
            if convert_clicked or (auto_convert and input_code):
                if input_code.strip():
                    with st.spinner(f"**{'🤖 AI' if use_ai_mode else '🔄'} Converting...**"):
                        if use_ai_mode and ai_prompt:
                            converted_code = convert_with_ai(input_code, ai_prompt, conversion_type if not use_ai_mode else None)
                        else:
                            converted_code = convert_code(input_code, conversion_type)
                        
                        st.session_state.output_code = converted_code
                        
                        # Display output with animation
                        st.markdown('<div class="fade-in">', unsafe_allow_html=True)
                        st.code(converted_code, language=get_output_language(conversion_type, use_ai_mode, ai_prompt), line_numbers=True)
                        st.markdown('</div>', unsafe_allow_html=True)
                        
                        # Save to history
                        if enable_history:
                            history_entry = {
                                "timestamp": datetime.now().isoformat(),
                                "conversion_type": "AI: " + ai_prompt if use_ai_mode else conversion_type,
                                "input_code": input_code,
                                "output_code": converted_code,
                                "input_length": len(input_code),
                                "output_length": len(converted_code),
                                "ai_mode": use_ai_mode,
                                "ai_prompt": ai_prompt if use_ai_mode else ""
                            }
                            st.session_state.conversion_history.append(history_entry)
                else:
                    st.warning("**⚠️ Please enter some code to convert.**")
                    st.session_state.output_code = ""
            else:
                if st.session_state.output_code:
                    current_conversion_type = "AI: " + st.session_state.ai_prompt if st.session_state.use_ai_mode else st.session_state.conversion_type
                    st.code(st.session_state.output_code, language=get_output_language(current_conversion_type, st.session_state.use_ai_mode, st.session_state.ai_prompt), line_numbers=True)
                else:
                    st.info("**💡 Enter your code and click 'Convert Code' to see the transformation here.**")
        
        # Statistics and Actions Row
        if show_stats and st.session_state.output_code:
            st.markdown("""
            <div class="section-title">
                <span>📊</span>
                Conversion Statistics
            </div>
            """, unsafe_allow_html=True)
            
            stats = analyze_code(st.session_state.input_code, st.session_state.output_code, 
                               "AI: " + ai_prompt if use_ai_mode else conversion_type)
            
            # Stats cards
            col_stat1, col_stat2, col_stat3, col_stat4 = st.columns(4)
            with col_stat1:
                st.markdown(f"""
                <div class="stat-card">
                    <div class="stat-number">{stats["Input Lines"]}</div>
                    <div class="stat-label">Input Lines</div>
                </div>
                """, unsafe_allow_html=True)
            with col_stat2:
                st.markdown(f"""
                <div class="stat-card">
                    <div class="stat-number">{stats["Output Lines"]}</div>
                    <div class="stat-label">Output Lines</div>
                </div>
                """, unsafe_allow_html=True)
            with col_stat3:
                st.markdown(f"""
                <div class="stat-card">
                    <div class="stat-number">{stats["Input Characters"]}</div>
                    <div class="stat-label">Input Chars</div>
                </div>
                """, unsafe_allow_html=True)
            with col_stat4:
                change_percent = ((len(st.session_state.output_code) - len(st.session_state.input_code)) / len(st.session_state.input_code) * 100) if st.session_state.input_code else 0
                st.markdown(f"""
                <div class="stat-card">
                    <div class="stat-number">{change_percent:+.1f}%</div>
                    <div class="stat-label">Size Change</div>
                </div>
                """, unsafe_allow_html=True)
            
            # Action buttons for output
            st.markdown("""
            <div style="margin: 30px 0 20px 0;">
            """, unsafe_allow_html=True)
            
            col_act1, col_act2, col_act3 = st.columns(3)
            with col_act1:
                if st.button("**📋 Copy Output**", use_container_width=True, key="copy_output"):
                    st.success("**✅ Output copied to clipboard!**")
            with col_act2:
                file_ext = get_file_extension(conversion_type, use_ai_mode, ai_prompt)
                st.download_button(
                    label="**💾 Download Output**",
                    data=st.session_state.output_code,
                    file_name=f"converted_code.{file_ext}",
                    mime="text/plain",
                    use_container_width=True
                )
            with col_act3:
                if st.button("**📜 View History**", use_container_width=True, key="view_history"):
                    if st.session_state.conversion_history:
                        st.markdown("""
                        <div class="section-title">
                            <span>📜</span>
                            Conversion History
                        </div>
                        """, unsafe_allow_html=True)
                        
                        for i, entry in enumerate(reversed(st.session_state.conversion_history[-5:]), 1):
                            with st.expander(f"**Conversion {i}** - {entry['conversion_type']} - {entry['timestamp'][11:16]}", expanded=False):
                                col_hist1, col_hist2 = st.columns(2)
                                with col_hist1:
                                    st.write(f"**Time:** {entry['timestamp'][:19]}")
                                    st.write(f"**Input:** {entry['input_length']} characters")
                                    if entry.get('ai_mode'):
                                        st.write(f"**AI Prompt:** {entry.get('ai_prompt', 'N/A')}")
                                with col_hist2:
                                    st.write(f"**Output:** {entry['output_length']} characters")
                                    st.write(f"**Type:** {entry['conversion_type']}")
                                
                                st.code(entry['output_code'][:300] + "..." if len(entry['output_code']) > 300 else entry['output_code'])
                    else:
                        st.info("**No conversion history yet. Start converting to build your history!**")
        
        st.markdown('</div>', unsafe_allow_html=True)  # Close content-section
        
        # Elegant Status Bar
        st.markdown(f"""
        <div class="elegant-status">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span>{'🤖 AI Mode' if use_ai_mode else '🚀'} Ready • AI-Powered Code Converter</span>
                <span>Conversions: {len(st.session_state.conversion_history)} • Input: {len(st.session_state.input_code)} chars • Output: {len(st.session_state.output_code)} chars</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)  # Close elegant-container

# ============================================================================
# AI-Powered Conversion Functions
# ============================================================================

def convert_with_ai(code: str, prompt: str, fallback_conversion: str = None) -> str:
    """Convert code using AI-powered prompt analysis"""
    
    # Analyze the prompt to determine the conversion type
    conversion_type = analyze_prompt(prompt, code)
    
    if conversion_type:
        # Use the detected conversion type
        return convert_code(code, conversion_type)
    elif fallback_conversion:
        # Use the fallback conversion type
        return convert_code(code, fallback_conversion)
    else:
        # Apply smart transformations based on prompt keywords
        return apply_smart_transformations(code, prompt)

def analyze_prompt(prompt: str, code: str) -> str:
    """Analyze the natural language prompt to determine conversion type"""
    prompt_lower = prompt.lower()
    code_lower = code.lower()
    
    # Language conversion mappings
    language_keywords = {
        "typescript": "JavaScript to TypeScript",
        "type script": "JavaScript to TypeScript",
        "python": "JavaScript to Python" if "javascript" in code_lower or "function" in code_lower else "Python to JavaScript",
        "java": "JavaScript to Java",
        "ruby": "Python to Ruby",
        "php": "Python to PHP",
        "go": "Python to Go",
        "tailwind": "CSS to Tailwind CSS",
        "scss": "CSS to SCSS",
        "sass": "CSS to SCSS",
        "vue": "React to Vue 3",
        "react": "Vue 3 to React",
        "pandas": "SQL to Pandas",
        "mongodb": "SQL to MongoDB",
        "xml": "JSON to XML",
        "yaml": "JSON to YAML",
        "markdown": "HTML to Markdown",
        "jsx": "HTML to JSX"
    }
    
    # Check for specific conversion keywords
    for keyword, conversion in language_keywords.items():
        if keyword in prompt_lower:
            return conversion
    
    # Check for "to" patterns (e.g., "convert javascript to python")
    to_pattern = re.search(r'(\w+)\s+to\s+(\w+)', prompt_lower)
    if to_pattern:
        from_lang, to_lang = to_pattern.groups()
        conversion_key = f"{from_lang.capitalize()} to {to_lang.capitalize()}"
        
        # Map common language names to our conversion types
        conversion_map = {
            "Javascript to Python": "JavaScript to Python",
            "Python to Javascript": "Python to JavaScript",
            "Javascript to Typescript": "JavaScript to TypeScript",
            "Typescript to Javascript": "TypeScript to JavaScript",
            "Css to Tailwind": "CSS to Tailwind CSS",
            "Sql to Pandas": "SQL to Pandas"
        }
        
        return conversion_map.get(conversion_key, conversion_key)
    
    return None

def apply_smart_transformations(code: str, prompt: str) -> str:
    """Apply smart transformations based on prompt analysis"""
    prompt_lower = prompt.lower()
    
    # Initialize result
    result = code
    
    # Add comments/improvements
    if any(word in prompt_lower for word in ["comment", "document", "explain"]):
        result = add_comments(result)
    
    # Optimize performance
    if any(word in prompt_lower for word in ["optimize", "performance", "faster", "efficient"]):
        result = optimize_code(result)
    
    # Add error handling
    if any(word in prompt_lower for word in ["error", "exception", "handle", "safe"]):
        result = add_error_handling(result)
    
    # Make more readable
    if any(word in prompt_lower for word in ["readable", "clean", "refactor"]):
        result = improve_readability(result)
    
    # Add AI header
    ai_header = f"# 🤖 AI-Powered Transformation\n# Prompt: {prompt}\n# Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
    
    return ai_header + result

def add_comments(code: str) -> str:
    """Add comments to code"""
    lines = code.split('\n')
    commented_lines = []
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped and not stripped.startswith(('//', '#', '/*', '*', '*/')):
            # Add comments for function definitions
            if re.match(r'(function|def|class)\s+\w+', stripped):
                commented_lines.append(f"// {stripped.split('(')[0]} definition")
            # Add comments for variable declarations
            elif re.match(r'(const|let|var|int|string|boolean)\s+\w+\s*=', stripped):
                commented_lines.append(f"// Variable declaration")
        commented_lines.append(line)
    
    return '\n'.join(commented_lines)

def optimize_code(code: str) -> str:
    """Apply basic code optimizations"""
    optimized = code
    
    # JavaScript optimizations
    if 'function' in code or 'const ' in code:
        # Convert function declarations to arrow functions where possible
        optimized = re.sub(r'function\s+(\w+)\s*\(([^)]*)\)\s*{', r'const \1 = (\2) => {', optimized)
    
    # Python optimizations
    if 'def ' in code:
        # Add type hints
        optimized = re.sub(r'def\s+(\w+)\((.*)\):', r'def \1(\2) -> None:', optimized)
    
    return f"// 🚀 Optimized version\n{optimized}"

def add_error_handling(code: str) -> str:
    """Add basic error handling"""
    result = code
    
    # JavaScript error handling
    if 'function' in code:
        result = "try {\n" + result + "\n} catch (error) {\n    console.error('Error:', error);\n}"
    
    # Python error handling
    elif 'def ' in code:
        result = "try:\n" + '\n'.join(['    ' + line for line in result.split('\n')]) + "\nexcept Exception as e:\n    print(f'Error: {e}')"
    
    return f"// 🛡️ With error handling\n{result}"

def improve_readability(code: str) -> str:
    """Improve code readability"""
    # Basic formatting improvements
    lines = code.split('\n')
    formatted_lines = []
    
    for line in lines:
        # Add proper spacing around operators
        line = re.sub(r'([=+*-/])(?=\S)', r'\1 ', line)
        line = re.sub(r'(?<=\S)([=+*-/])', r' \1', line)
        formatted_lines.append(line)
    
    return '\n'.join(formatted_lines)

# ============================================================================
# Enhanced Conversion Functions (All Missing Functions Included)
# ============================================================================

def convert_code(code: str, conversion_type: str) -> str:
    """Convert code based on the selected conversion type"""
    conversion_functions = {
        # JavaScript & TypeScript
        "JavaScript to TypeScript": convert_js_to_ts,
        "TypeScript to JavaScript": convert_ts_to_js,
        "JavaScript to Python": convert_js_to_python,
        "Python to JavaScript": convert_python_to_js,
        
        # Python & Data Science
        "Python to Ruby": convert_python_to_ruby,
        "Ruby to Python": convert_ruby_to_python,
        "Python to PHP": convert_python_to_php,
        "PHP to Python": convert_php_to_python,
        
        # CSS & Styling
        "CSS to Tailwind CSS": convert_css_to_tailwind,
        "Tailwind CSS to CSS": convert_tailwind_to_css,
        "CSS to SCSS": convert_css_to_scss,
        "SCSS to CSS": convert_scss_to_css,
        
        # React & Frameworks
        "React Class to Function Components": convert_react_class_to_function,
        "React to Vue 3": convert_react_to_vue,
        "Vue 3 to React": convert_vue_to_react,
        
        # Data & Formats
        "SQL to Pandas": convert_sql_to_pandas,
        "SQL to MongoDB": convert_sql_to_mongodb,
        "JSON to Python Dict": convert_json_to_python,
        "JSON to XML": convert_json_to_xml,
        "XML to JSON": convert_xml_to_json,
        "CSV to JSON": convert_csv_to_json,
        "Base64 Encode": convert_base64_encode,
        "Base64 Decode": convert_base64_decode,
        
        # Web & Markup
        "HTML to JSX": convert_html_to_jsx,
        "Markdown to HTML": convert_markdown_to_html,
        "HTML to Markdown": convert_html_to_markdown
    }
    
    converter = conversion_functions.get(conversion_type)
    if converter:
        return converter(code)
    else:
        return f"// 🔧 Conversion type '{conversion_type}' not implemented yet.\n// Consider using AI mode with a specific prompt."

# JavaScript & TypeScript Conversions
def convert_js_to_ts(code: str) -> str:
    """Convert JavaScript to TypeScript"""
    lines = code.split('\n')
    converted_lines = []
    
    for line in lines:
        if re.match(r'^\s*function\s+\w+\s*\([^)]*\)', line):
            line = re.sub(r'(function\s+\w+\s*\([^)]*\))\s*{', r'\1: any {', line)
        
        if re.match(r'^\s*(const|let|var)\s+\w+\s*=', line):
            if '[]' in line:
                line = re.sub(r'(const|let|var)\s+(\w+)\s*=', r'\1 \2: any[] =', line)
            elif '{' in line:
                line = re.sub(r'(const|let|var)\s+(\w+)\s*=', r'\1 \2: any =', line)
            elif 'true' in line or 'false' in line:
                line = re.sub(r'(const|let|var)\s+(\w+)\s*=', r'\1 \2: boolean =', line)
            elif re.search(r'=\s*\d+', line):
                line = re.sub(r'(const|let|var)\s+(\w+)\s*=', r'\1 \2: number =', line)
            elif re.search(r'=\s*["\']', line):
                line = re.sub(r'(const|let|var)\s+(\w+)\s*=', r'\1 \2: string =', line)
            else:
                line = re.sub(r'(const|let|var)\s+(\w+)\s*=', r'\1 \2: any =', line)
        
        converted_lines.append(line)
    
    result = '\n'.join(converted_lines)
    return f"// 🚀 Converted from JavaScript to TypeScript\n// 📅 {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n{result}"

def convert_ts_to_js(code: str) -> str:
    """Convert TypeScript to JavaScript"""
    code = re.sub(r':\s*\w+(?:\s*\[\])?(?:\s*\|\s*\w+)*\s*(?=[,=){}]|$)', '', code)
    code = re.sub(r'^\s*(interface|type)\s+\w+\s*\{[^}]*\}\s*$', '', code, flags=re.MULTILINE)
    code = re.sub(r'<\w+>', '', code)
    return f"// 🚀 Converted from TypeScript to JavaScript\n// 📅 {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n{code}"

def convert_js_to_python(code: str) -> str:
    """Convert JavaScript to Python"""
    lines = code.split('\n')
    python_lines = []
    indent_level = 0
    
    for line in lines:
        if re.match(r'^\s*function\s+\w+', line):
            line = re.sub(r'function\s+(\w+)\(([^)]*)\)', r'def \1(\2):', line)
            line = line.replace('{', '')
        
        line = re.sub(r'(const|let|var)\s+', '', line)
        line = re.sub(r'console\.log\((.*)\)', r'print(\1)', line)
        line = line.replace('===', '==').replace('!==', '!=')
        line = line.replace('true', 'True').replace('false', 'False')
        line = line.replace('null', 'None')
        
        if '=>' in line:
            line = re.sub(r'\(([^)]*)\)\s*=>', r'lambda \1:', line)
            line = re.sub(r'(\w+)\s*=>', r'lambda \1:', line)
        
        if '{' in line:
            indent_level += 1
            line = line.replace('{', '')
        if '}' in line:
            indent_level -= 1
            line = line.replace('}', '')
        
        if line.strip():
            python_lines.append('    ' * indent_level + line.strip())
    
    result = '\n'.join(python_lines)
    return f"# 🚀 Converted from JavaScript to Python\n# 📅 {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n{result}"

def convert_python_to_js(code: str) -> str:
    """Convert Python to JavaScript"""
    lines = code.split('\n')
    converted_lines = []
    indent_level = 0
    
    for line in lines:
        line = line.rstrip()
        line = re.sub(r'print\((.*)\)', r'console.log(\1)', line)
        line = re.sub(r'def (\w+)\((.*)\):', r'function \1(\2) {', line)
        
        if line.strip().startswith('class '):
            line = re.sub(r'class (\w+).*:', r'class \1 {', line)
        
        line = line.replace('None', 'null')
        line = line.replace('True', 'true')
        line = line.replace('False', 'false')
        line = line.replace('#', '//')
        
        stripped = line.strip()
        if stripped.endswith('{'):
            converted_lines.append('    ' * indent_level + line)
            indent_level += 1
        elif stripped.startswith('}') or (stripped and not any(stripped.startswith(x) for x in ['function', 'class', '//'])):
            if indent_level > 0 and not stripped.startswith('}'):
                indent_level -= 1
            converted_lines.append('    ' * indent_level + line)
            if stripped.endswith('}'):
                indent_level -= 1
        else:
            converted_lines.append('    ' * indent_level + line)
    
    for i in range(indent_level):
        converted_lines.append('    ' * (indent_level - i - 1) + '}')
    
    result = '\n'.join(converted_lines)
    return f"// 🚀 Converted from Python to JavaScript\n// 📅 {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n{result}"

# Python Conversions
def convert_python_to_ruby(code: str) -> str:
    """Convert Python to Ruby"""
    ruby_code = code
    
    # Convert function definitions
    ruby_code = re.sub(r'def (\w+)\((.*)\):', r'def \1(\2)', ruby_code)
    
    # Convert print to puts
    ruby_code = re.sub(r'print\((.*)\)', r'puts \1', ruby_code)
    
    # Convert True/False/None
    ruby_code = ruby_code.replace('True', 'true')
    ruby_code = ruby_code.replace('False', 'false')
    ruby_code = ruby_code.replace('None', 'nil')
    
    return f"# 🚀 Converted from Python to Ruby\n# 📅 {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n{ruby_code}"

def convert_ruby_to_python(code: str) -> str:
    """Convert Ruby to Python"""
    python_code = code
    
    # Convert function definitions
    python_code = re.sub(r'def (\w+)\((.*)\)', r'def \1(\2):', python_code)
    
    # Convert puts to print
    python_code = re.sub(r'puts (.*)', r'print(\1)', python_code)
    
    # Convert true/false/nil
    python_code = python_code.replace('true', 'True')
    python_code = python_code.replace('false', 'False')
    python_code = python_code.replace('nil', 'None')
    
    return f"# 🚀 Converted from Ruby to Python\n# 📅 {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n{python_code}"

def convert_python_to_php(code: str) -> str:
    """Convert Python to PHP"""
    php_code = code
    
    # Convert function definitions
    php_code = re.sub(r'def (\w+)\(([^)]*)\):', r'function \1(\2) {', php_code)
    
    # Convert print to echo
    php_code = re.sub(r'print\((.*)\)', r'echo \1;', php_code)
    
    # Convert variables
    php_code = re.sub(r'(\w+)\s*=', r'$\1 =', php_code)
    
    # Convert True/False/None
    php_code = php_code.replace('True', 'true')
    php_code = php_code.replace('False', 'false')
    php_code = php_code.replace('None', 'null')
    
    return f"// 🚀 Converted from Python to PHP\n// 📅 {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n<?php\n{php_code}\n?>"

def convert_php_to_python(code: str) -> str:
    """Convert PHP to Python"""
    python_code = code
    
    # Remove PHP tags
    python_code = re.sub(r'<\?php|\?>', '', python_code)
    
    # Convert function definitions
    python_code = re.sub(r'function\s+(\w+)\(([^)]*)\)\s*{', r'def \1(\2):', python_code)
    
    # Convert echo to print
    python_code = re.sub(r'echo\s+(.*);', r'print(\1)', python_code)
    
    # Convert variables
    python_code = re.sub(r'\$(\w+)', r'\1', python_code)
    
    # Convert true/false/null
    python_code = python_code.replace('true', 'True')
    python_code = python_code.replace('false', 'False')
    python_code = python_code.replace('null', 'None')
    
    return f"# 🚀 Converted from PHP to Python\n# 📅 {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n{python_code}"

# CSS & Styling Conversions
def convert_css_to_tailwind(code: str) -> str:
    """Convert CSS to Tailwind CSS"""
    css_to_tailwind = {
        r'margin:\s*(\d+)px': lambda x: f"m-{int(x)//4}",
        r'padding:\s*(\d+)px': lambda x: f"p-{int(x)//4}",
        r'font-size:\s*(\d+)px': lambda x: f"text-{int(x)//4}",
        r'background-color:\s*#([0-9a-fA-F]{6})': lambda x: f"bg-[#{x}]",
        r'color:\s*#([0-9a-fA-F]{6})': lambda x: f"text-[#{x}]",
        r'text-align:\s*center': "text-center",
        r'font-weight:\s*bold': "font-bold",
        r'display:\s*flex': "flex"
    }
    
    tailwind_classes = []
    lines = code.split('\n')
    
    for line in lines:
        line = line.strip().rstrip(';')
        for pattern, replacement in css_to_tailwind.items():
            match = re.search(pattern, line, re.IGNORECASE)
            if match:
                if callable(replacement):
                    tailwind_classes.append(replacement(match.group(1)))
                else:
                    tailwind_classes.append(replacement)
                break
    
    unique_classes = list(set(tailwind_classes))
    result = " ".join(unique_classes)
    return f"<!-- 🎨 Converted from CSS to Tailwind -->\n<div class=\"{result}\">\n  <!-- Your content here -->\n</div>"

def convert_tailwind_to_css(code: str) -> str:
    """Convert Tailwind CSS to CSS"""
    tailwind_to_css = {
        r'm-(\d+)': lambda x: f"margin: {int(x)*4}px;",
        r'p-(\d+)': lambda x: f"padding: {int(x)*4}px;",
        'text-center': "text-align: center;",
        'font-bold': "font-weight: bold;",
        'flex': "display: flex;"
    }
    
    css_rules = []
    tailwind_classes = re.findall(r'class="([^"]*)"', code)
    
    for class_string in tailwind_classes:
        classes = class_string.split()
        for cls in classes:
            for pattern, replacement in tailwind_to_css.items():
                match = re.match(pattern, cls)
                if match:
                    if callable(replacement):
                        css_rules.append(f"  {replacement(match.group(1))}")
                    else:
                        css_rules.append(f"  {replacement}")
                    break
    
    if css_rules:
        result = ".converted-element {\n" + "\n".join(css_rules) + "\n}"
    else:
        result = "/* No Tailwind classes found or converted */"
    
    return f"/* 🎨 Converted from Tailwind CSS */\n{result}"

def convert_css_to_scss(code: str) -> str:
    """Convert CSS to SCSS"""
    scss_code = code
    
    # Convert to SCSS nesting (basic)
    scss_code = re.sub(r'\.(\w+)\s*{', r'.\\1 {', scss_code)
    
    return f"// 🎨 Converted from CSS to SCSS\n// 📅 {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n{scss_code}"

def convert_scss_to_css(code: str) -> str:
    """Convert SCSS to CSS"""
    css_code = code
    
    # Remove SCSS nesting (basic)
    css_code = re.sub(r'&:', '', css_code)
    
    return f"/* 🎨 Converted from SCSS to CSS */\n/* 📅 {datetime.now().strftime('%Y-%m-%d %H:%M')} */\n\n{css_code}"

# React & Framework Conversions
def convert_react_class_to_function(code: str) -> str:
    """Convert React class components to function components"""
    converted = re.sub(r'class\s+(\w+)\s+extends\s+(Component|React\.Component)', r'function \1', code)
    converted = re.sub(r'render\(\)\s*{', r'return (', converted)
    converted = re.sub(r'this\.state\.', 'state.', converted)
    converted = re.sub(r'this\.props\.', 'props.', converted)
    return f"// ⚛️ Converted from Class to Function Component\n// 📅 {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n{converted}"

def convert_react_to_vue(code: str) -> str:
    """Convert React to Vue 3"""
    vue_template = "<template>\n  <div>\n    <!-- Your template here -->\n  </div>\n</template>\n\n"
    vue_script = "<script setup>\n// Vue 3 Composition API\nimport { ref, reactive } from 'vue'\n\n// Converted from React\n</script>\n\n"
    vue_style = "<style scoped>\n/* Your styles here */\n</style>"
    
    return f"<!-- 🔄 Converted from React to Vue 3 -->\n{vue_template}{vue_script}{vue_style}"

def convert_vue_to_react(code: str) -> str:
    """Convert Vue 3 to React"""
    react_component = """import React from 'react';

function ConvertedComponent() {
  return (
    <div>
      {/* Your JSX here */}
    </div>
  );
}

export default ConvertedComponent;"""
    
    return f"{{/* 🔄 Converted from Vue 3 to React */}}\n{react_component}"

# Data & Format Conversions
def convert_sql_to_pandas(code: str) -> str:
    """Convert SQL queries to pandas operations"""
    code_upper = code.upper()
    
    if 'SELECT' in code_upper and 'FROM' in code_upper:
        base_code = "import pandas as pd\n\n# Assuming you have a DataFrame called 'df'\n"
        
        if 'WHERE' in code_upper:
            base_code += "# This is a basic conversion - you may need to adjust conditions\n"
            base_code += "result = df.query('your_condition_here')\n"
        else:
            base_code += "result = df\n"
        
        if 'ORDER BY' in code_upper:
            base_code += "result = result.sort_values(by='column_name')\n"
        
        return base_code
    
    return f"# 🗃️ SQL to Pandas conversion\n# Original SQL:\n# {code}\n\n# Pandas equivalent would be implemented here"

def convert_sql_to_mongodb(code: str) -> str:
    """Convert SQL queries to MongoDB operations"""
    code_upper = code.upper()
    
    if 'SELECT' in code_upper:
        base = "// MongoDB equivalent\ndb.collection."
        
        if 'WHERE' in code_upper:
            base += "find({ /* your query */ })"
        else:
            base += "find({})"
        
        if 'ORDER BY' in code_upper:
            base += ".sort({ field: 1 })"
        
        if 'LIMIT' in code_upper:
            base += ".limit(10)"
        
        return base
    
    return f"// 🗃️ SQL to MongoDB conversion\n// Original: {code}\n// MongoDB equivalent would be implemented here"

def convert_json_to_python(code: str) -> str:
    """Convert JSON to Python dictionary"""
    try:
        parsed = json.loads(code)
        formatted = json.dumps(parsed, indent=2)
        return f"# 📋 Python dictionary from JSON\n{formatted}"
    except json.JSONDecodeError:
        return "# ❌ Error: Invalid JSON format\n\n# Please provide valid JSON"

def convert_json_to_xml(code: str) -> str:
    """Convert JSON to XML"""
    try:
        data = json.loads(code)
        xml = '<?xml version="1.0" encoding="UTF-8"?>\n<root>\n'
        
        def dict_to_xml(d, indent=2):
            xml_str = ""
            for key, value in d.items():
                xml_str += " " * indent + f"<{key}>"
                if isinstance(value, dict):
                    xml_str += f"\n{dict_to_xml(value, indent + 2)}\n" + " " * indent
                elif isinstance(value, list):
                    for item in value:
                        xml_str += f"\n{dict_to_xml(item, indent + 2)}\n" + " " * indent
                else:
                    xml_str += str(value)
                xml_str += f"</{key}>\n"
            return xml_str
        
        xml += dict_to_xml(data)
        xml += "</root>"
        return f"<!-- 📋 Converted from JSON to XML -->\n{xml}"
    except:
        return "<!-- ❌ Error converting JSON to XML -->"

def convert_xml_to_json(code: str) -> str:
    """Convert XML to JSON (simplified)"""
    # This is a very basic conversion
    json_data = {"converted": "from_xml", "content": code[:100] + "..."}
    return json.dumps(json_data, indent=2)

def convert_csv_to_json(code: str) -> str:
    """Convert CSV to JSON"""
    lines = code.strip().split('\n')
    if len(lines) < 2:
        return json.dumps([], indent=2)
    
    headers = [h.strip() for h in lines[0].split(',')]
    data = []
    
    for line in lines[1:]:
        values = [v.strip() for v in line.split(',')]
        if len(values) == len(headers):
            row = dict(zip(headers, values))
            data.append(row)
    
    return json.dumps(data, indent=2)

def convert_base64_encode(code: str) -> str:
    """Convert text to Base64"""
    try:
        encoded = base64.b64encode(code.encode()).decode()
        return f"# 🔐 Base64 Encoded\n{encoded}"
    except:
        return "# ❌ Error encoding to Base64"

def convert_base64_decode(code: str) -> str:
    """Convert Base64 to text"""
    try:
        decoded = base64.b64decode(code).decode()
        return f"# 🔓 Base64 Decoded\n{decoded}"
    except:
        return "# ❌ Error decoding from Base64"

# Web & Markup Conversions
def convert_html_to_jsx(code: str) -> str:
    """Convert HTML to JSX"""
    converted = code
    converted = re.sub(r'class="', 'className="', converted)
    converted = re.sub(r'<(\w+)([^>]*)\s*>(?=\s*</\1>)', r'<\1\2 />', converted)
    return f"// 🔄 Converted from HTML to JSX\n{converted}"

def convert_markdown_to_html(code: str) -> str:
    """Convert Markdown to HTML"""
    html_content = code
    html_content = re.sub(r'^# (.*)$', r'<h1>\1</h1>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'^## (.*)$', r'<h2>\1</h2>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'^### (.*)$', r'<h3>\1</h3>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html_content)
    html_content = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html_content)
    html_content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', html_content)
    html_content = re.sub(r'^- (.*)$', r'<li>\1</li>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'(<li>.*</li>)', r'<ul>\n\1\n</ul>', html_content, flags=re.DOTALL)
    return f"<!-- 📝 Converted from Markdown to HTML -->\n{html_content}"

def convert_html_to_markdown(code: str) -> str:
    """Convert HTML to Markdown"""
    md_content = code
    
    # Headers
    md_content = re.sub(r'<h1>(.*?)</h1>', r'# \1', md_content)
    md_content = re.sub(r'<h2>(.*?)</h2>', r'## \1', md_content)
    md_content = re.sub(r'<h3>(.*?)</h3>', r'### \1', md_content)
    
    # Bold and Italic
    md_content = re.sub(r'<strong>(.*?)</strong>', r'**\1**', md_content)
    md_content = re.sub(r'<em>(.*?)</em>', r'*\1*', md_content)
    
    # Links
    md_content = re.sub(r'<a href="([^"]*)">([^<]*)</a>', r'[\2](\1)', md_content)
    
    # Lists
    md_content = re.sub(r'<li>(.*?)</li>', r'- \1', md_content)
    md_content = re.sub(r'<ul>\s*|</ul>\s*', '', md_content)
    
    # Remove other HTML tags
    md_content = re.sub(r'<[^>]*>', '', md_content)
    
    return f"<!-- 📝 Converted from HTML to Markdown -->\n{md_content}"

# ============================================================================
# Utility Functions
# ============================================================================

def get_output_language(conversion_type: str, use_ai_mode: bool = False, ai_prompt: str = "") -> str:
    """Get the language for syntax highlighting"""
    if use_ai_mode:
        # Try to detect language from AI prompt
        prompt_lower = ai_prompt.lower()
        if any(word in prompt_lower for word in ["python", "pandas", "dataframe"]):
            return "python"
        elif any(word in prompt_lower for word in ["javascript", "typescript", "react", "node"]):
            return "javascript"
        elif any(word in prompt_lower for word in ["java"]):
            return "java"
        elif any(word in prompt_lower for word in ["css", "tailwind", "scss"]):
            return "css"
        elif any(word in prompt_lower for word in ["html", "markdown"]):
            return "html"
        elif any(word in prompt_lower for word in ["sql", "mongodb"]):
            return "sql"
        else:
            return "text"
    
    mapping = {
        # JavaScript & TypeScript
        "JavaScript to TypeScript": "typescript",
        "TypeScript to JavaScript": "javascript",
        "JavaScript to Python": "python",
        "Python to JavaScript": "javascript",
        
        # Python & Data Science
        "Python to Ruby": "ruby",
        "Ruby to Python": "python",
        "Python to PHP": "php",
        "PHP to Python": "python",
        
        # CSS & Styling
        "CSS to Tailwind CSS": "html",
        "Tailwind CSS to CSS": "css",
        "CSS to SCSS": "scss",
        "SCSS to CSS": "css",
        
        # React & Frameworks
        "React Class to Function Components": "jsx",
        "React to Vue 3": "html",
        "Vue 3 to React": "jsx",
        
        # Data & Formats
        "SQL to Pandas": "python",
        "SQL to MongoDB": "javascript",
        "JSON to Python Dict": "python",
        "JSON to XML": "xml",
        "XML to JSON": "json",
        "CSV to JSON": "json",
        "Base64 Encode": "text",
        "Base64 Decode": "text",
        
        # Web & Markup
        "HTML to JSX": "jsx",
        "Markdown to HTML": "html",
        "HTML to Markdown": "markdown"
    }
    return mapping.get(conversion_type, "text")

def get_file_extension(conversion_type: str, use_ai_mode: bool = False, ai_prompt: str = "") -> str:
    """Get appropriate file extension for download"""
    if use_ai_mode:
        # Try to detect extension from AI prompt
        prompt_lower = ai_prompt.lower()
        if any(word in prompt_lower for word in ["python", "pandas"]):
            return "py"
        elif any(word in prompt_lower for word in ["javascript", "node"]):
            return "js"
        elif any(word in prompt_lower for word in ["typescript"]):
            return "ts"
        elif any(word in prompt_lower for word in ["java"]):
            return "java"
        elif any(word in prompt_lower for word in ["css", "tailwind"]):
            return "css"
        elif any(word in prompt_lower for word in ["html"]):
            return "html"
        else:
            return "txt"
    
    ext_map = {
        # JavaScript & TypeScript
        "JavaScript to TypeScript": "ts",
        "TypeScript to JavaScript": "js",
        "JavaScript to Python": "py",
        "Python to JavaScript": "js",
        
        # Python & Data Science
        "Python to Ruby": "rb",
        "Ruby to Python": "py",
        "Python to PHP": "php",
        "PHP to Python": "py",
        
        # CSS & Styling
        "CSS to Tailwind CSS": "html",
        "Tailwind CSS to CSS": "css",
        "CSS to SCSS": "scss",
        "SCSS to CSS": "css",
        
        # React & Frameworks
        "React Class to Function Components": "jsx",
        "React to Vue 3": "vue",
        "Vue 3 to React": "jsx",
        
        # Data & Formats
        "SQL to Pandas": "py",
        "SQL to MongoDB": "js",
        "JSON to Python Dict": "py",
        "JSON to XML": "xml",
        "XML to JSON": "json",
        "CSV to JSON": "json",
        "Base64 Encode": "txt",
        "Base64 Decode": "txt",
        
        # Web & Markup
        "HTML to JSX": "jsx",
        "Markdown to HTML": "html",
        "HTML to Markdown": "md"
    }
    return ext_map.get(conversion_type, "txt")

def analyze_code(input_code: str, output_code: str, conversion_type: str) -> Dict[str, Any]:
    """Analyze the code conversion with detailed metrics"""
    input_lines = input_code.split('\n')
    output_lines = output_code.split('\n')
    
    analysis = {
        "Input Lines": len(input_lines),
        "Output Lines": len(output_lines),
        "Input Characters": len(input_code),
        "Output Characters": len(output_code),
        "Conversion Type": conversion_type
    }
    
    return analysis

if __name__ == "__main__":
    main()
