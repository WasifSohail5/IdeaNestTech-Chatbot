# 🚀 IdeaNestTech AI Chatbot

> *Powered by Google's **Gemini-1.5-Flash** - The intelligent virtual assistant for your digital innovation needs*

![IdeaNestTech Banner](https://www.ideanesttech.com/assets/img/logo.png)

## 💫 Overview

Welcome to the official **AI-powered chatbot** built for [IdeaNestTech](https://www.ideanesttech.com) — a full-stack digital innovation company transforming ideas into reality through modern tech solutions.

This intelligent assistant leverages **Google's cutting-edge Gemini-1.5-Flash model** combined with advanced retrieval-augmented generation (RAG) to provide precise, context-aware responses about our services, courses, and capabilities.

## 🧠 What Makes Our Chatbot Special

This isn't your average chatbot! Our AI assistant:

- 🔮 Uses **Gemini-1.5-Flash** - Google's most efficient multimodal model
- 🔍 Implements intelligent context retrieval using FAISS vector search
- ⚡ Delivers lightning-fast responses through optimized FastAPI backend
- 📚 Understands the complete IdeaNestTech ecosystem and service offerings
- 🛠️ Can be easily expanded with new capabilities and knowledge

## 🏢 About IdeaNestTech

> *Where innovation meets execution — bridging the gap between ideas and impactful digital solutions*

IdeaNestTech operates at the intersection of technology services, education, and startup empowerment. We're a hybrid digital agency that:

- 🌐 Serves clients globally with a strong presence across Pakistan
- 🚀 Incubates promising startups with mentorship and technical resources
- 🎓 Educates the next generation through our comprehensive Digital Academy

### ✨ Our Solutions Universe

| Service Category | Offerings |
|-----------------|-----------|
| **Development** | Full-stack Web & Mobile Apps, Custom Software, AI Solutions |
| **Design** | UI/UX, Brand Identity, Interactive Experiences |
| **Emerging Tech** | AI Chatbots, Machine Learning, Blockchain, IoT Integration |
| **Digital Presence** | SEO, Content Marketing, Social Media Management |
| **Gaming** | Unity 2D/3D Development, Game Design, Interactive Experiences |
| **Education** | Tech Bootcamps, Specialized Courses, Professional Certification |

## 🛠️ Technical Architecture

Our chatbot leverages a powerful tech stack:

```
Frontend ──────► API Gateway ──────► FastAPI Backend ──────► Gemini-1.5-Flash
                                          │
                                          ▼
                            ┌─────────────┴─────────────┐
                            │                           │
                     FAISS Vectorstore           Document Processor
                            │                           │
                            └─────────────┬─────────────┘
                                          │
                                          ▼
                                  Company Knowledge Base
```

### Core Technologies:
- **FastAPI**: High-performance Python web framework
- **Google Generative AI**: Accessing Gemini-1.5-Flash capabilities
- **Sentence Transformers**: Creating semantic embeddings with MiniLM
- **FAISS**: Facebook AI's efficient similarity search library
- **Python 3.9+**: Modern language features and async support

## 📂 Project Structure

```
├── chatbot_api.py          # FastAPI application entry point
├── retriever.py            # Vector embedding and retrieval logic
├── api_integration.py       # Gemini 1.5 Flash integration & prompt engineering
├── pdf_extractor.py        #extract pdf and creating chunks and embeddings
├── test.py            #testing script for backend working of chatbot
├── IdeaNestTech_Chatbot_Info.pdf  # Knowledge base document
├── ideanest_index.faiss    # Vectorized knowledge index
├── ideanest_chunks.pkl     # Preprocessed text chunks
└── ideanest_embedding_model/  # Model files for embeddings
```

## ▶️ Getting Started

### 1️⃣ Set Up Your Environment

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install fastapi uvicorn google-generativeai sentence-transformers faiss-cpu pydantic
```

### 2️⃣ Run the FastAPI Server

```bash
# Start the server with hot-reloading
uvicorn chatbot_api:app --reload --port 8000
```

### 3️⃣ Test the Chatbot

Navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to access the Swagger UI.
You can test the chatbot directly through this interface!

## 🔍 API Usage Example

### Request
```http
POST /chat HTTP/1.1
Content-Type: application/json

{
  "question": "What courses are available in the Digital Academy?",
  "api_key": "your-gemini-api-key"
}
```

### Response
```json
{
  "answer": "IdeaNestTech's Digital Academy offers a variety of tech-focused courses including: Full-Stack Web Development, UI/UX Design, Digital Marketing, Mobile App Development, Data Science Fundamentals, Game Development with Unity, and Cybersecurity Essentials. Each course combines theoretical knowledge with hands-on projects guided by industry experts. You can explore the full catalog at academy.ideanesttech.com.",
  "source_documents": ["academy_catalog.pdf", "services_overview.pdf"]
}
```

## 🌟 Upcoming Enhancements

We're continuously improving our chatbot with exciting new features:

- 🔄 **Multi-turn conversations** with memory of past interactions
- 📱 **Mobile-optimized interface** for on-the-go queries
- 🔐 **User authentication** for personalized responses
- 📊 **Analytics dashboard** for conversation insights
- 🌐 **Multilingual support** including Urdu, Arabic and Chinese
- 🤝 **Integration with CRM systems** for seamless lead management
- 🎭 **Customizable chatbot personality** to match brand voice

## 🔗 Connect With Us

- 🌐 **Website**: [ideanesttech.com](https://www.ideanesttech.com)
- 📧 **Email**: [info@ideanesttech.com](mailto:info@ideanesttech.com)
- 📱 **Phone**: +92 300 1234567
- 📍 **Location**: Islamabad, Pakistan (with remote teams worldwide)
- 💼 **LinkedIn**: [IdeaNestTech](https://www.linkedin.com/company/ideanesttech)
- 🐦 **Twitter**: [@IdeaNestTech](https://twitter.com/ideanesttech)

## 👨‍💻 Developed By

This advanced AI solution was engineered by Wasif Sohail.
