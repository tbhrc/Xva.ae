/**
 * AI Experts Data
 * Single source of truth for the AI Experts Directory.
 */

const expertsData = [
    {
        id: 'ignatius-rautenbach',
        name: 'Ignatius (Natie) Rautenbach',
        title: 'AI Strategy & Ethics',
        summary: 'Lead AI Strategist with 15+ years of experience. Expert in ethical AI, responsible AI implementation, and transforming complex data into actionable business insights.',
        expertise: ['AI Consultant', 'AI Strategy', 'Ethics'],
        location: 'Dubai, UAE',
        availabilityType: 'Advisory or fractional',
        tools: ['Ethical AI Frameworks', 'Data Strategy'],
        vettedStatus: 'Vetted',
        linkedinUrl: 'https://www.linkedin.com/in/natierau/',
        imageUrl: '../../assets/images/Ignatius (Natie) Rautenbach.jpg'
    },
    {
        id: 'christopher-booth',
        name: 'Christopher Booth',
        title: 'Generative AI & Product Ownership',
        summary: 'Specialist in Generative AI and conversational agents. Brings deep expertise in product ownership for large-scale AI deployments, including banking sector chatbots.',
        expertise: ['AI Product Manager', 'Prompt Engineer', 'Generative AI', 'Product Ownership'],
        location: 'Dubai, UAE',
        availabilityType: 'Project based or freelance',
        tools: ['Generative AI', 'Chatbots', 'Product Management'],
        vettedStatus: 'Vetted',
        linkedinUrl: 'https://www.linkedin.com/in/christopher--booth/',
        imageUrl: '../../assets/images/Christopher Booth.jpg'
    },
    {
        id: 'stephen-kruger',
        name: 'Stephen Kruger',
        title: 'CTO & Technology Leadership',
        summary: 'Former CTO of Careem and inDrive with 20 patents. Expert in platform architecture, cloud security, and scaling engineering teams for high-growth tech companies.',
        expertise: ['AI Consultant', 'Technology Leadership', 'CTO', 'Cloud Architecture'],
        location: 'Dubai, UAE',
        availabilityType: 'Advisory or fractional',
        tools: ['Cloud Architecture', 'Security', 'Scaling'],
        vettedStatus: 'Vetted',
        linkedinUrl: 'https://www.linkedin.com/in/stephen-kruger/',
        imageUrl: '../../assets/images/Stephen Kruger.jpg'
    },
    {
        id: 'sara-ali',
        name: 'Sara Al Mansoori',
        title: 'Automation engineer focused on finance ops and service triage',
        summary: 'Specializing in automating financial operations and service triage workflows to improve efficiency and reduce error rates.',
        expertise: ['Automation Engineer', 'AI Consultant'],
        location: 'Dubai, UAE',
        availabilityType: 'Project based or freelance',
        tools: ['Make', 'LangChain', 'Python', 'OpenAI'],
        vettedStatus: 'Vetted',
        linkedinUrl: '',
        imageUrl: ''
    },
    {
        id: 'omar-haddad',
        name: 'Omar Haddad',
        title: 'LLM engineer building RAG assistants and internal copilots',
        summary: 'Building robust RAG systems and internal copilots to empower teams with instant access to organizational knowledge.',
        expertise: ['LLM Engineer', 'Prompt Engineer'],
        location: 'Amman, Jordan',
        availabilityType: 'Advisory or fractional',
        tools: ['LangGraph', 'Pinecone', 'Azure OpenAI', 'Anthropic'],
        vettedStatus: 'Pending', // Assuming 'false' mapped to 'Pending' or similar, using 'Pending' for now or just not 'Vetted'
        linkedinUrl: '',
        imageUrl: ''
    },
    {
        id: 'fatima-khan',
        name: 'Fatima Khan',
        title: 'Data scientist with demand forecasting and NLP expertise',
        summary: 'Leveraging advanced NLP and demand forecasting models to drive data-informed decision making.',
        expertise: ['Data Scientist', 'ML Engineer'],
        location: 'Abu Dhabi, UAE',
        availabilityType: 'Part time, remote',
        tools: ['PyTorch', 'Vertex AI', 'BigQuery', 'Airflow'],
        vettedStatus: 'Vetted',
        linkedinUrl: '',
        imageUrl: ''
    },
    {
        id: 'daniel-choi',
        name: 'Daniel Choi',
        title: 'Full stack AI developer shipping production-ready front ends',
        summary: 'Creating seamless, production-ready front-end experiences for AI-powered applications.',
        expertise: ['AI Developer, Full stack', 'AI Developer, Front end'],
        location: 'Singapore',
        availabilityType: 'Project based or freelance',
        tools: ['Next.js', 'TypeScript', 'Vercel', 'Supabase'],
        vettedStatus: 'Pending',
        linkedinUrl: '',
        imageUrl: ''
    },
    {
        id: 'leila-hassan',
        name: 'Leila Hassan',
        title: 'AI product manager for regulated industries and compliance',
        summary: 'Navigating the complexities of AI product management within regulated industries, ensuring compliance and safety.',
        expertise: ['AI Product Manager', 'AI Consultant'],
        location: 'Riyadh, KSA',
        availabilityType: 'Advisory or fractional',
        tools: ['Jira', 'Figma', 'PromptOps', 'Datadog'],
        vettedStatus: 'Pending',
        linkedinUrl: '',
        imageUrl: ''
    },
    {
        id: 'james-ibrahim',
        name: 'James Ibrahim',
        title: 'MLOps engineer building reliable deployment pipelines',
        summary: 'Architecting and maintaining reliable MLOps pipelines to ensure smooth model deployment and monitoring.',
        expertise: ['MLOps Engineer', 'ML Engineer'],
        location: 'Dubai, UAE',
        availabilityType: 'Full time, remote',
        tools: ['Kubernetes', 'MLflow', 'Argo', 'Databricks'],
        vettedStatus: 'Vetted',
        linkedinUrl: '',
        imageUrl: ''
    }
];

// Export for usage if using modules, but for vanilla JS we'll just rely on the global variable or attach to window
window.expertsData = expertsData;
