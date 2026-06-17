DOMAIN_SUMMARY = 'PDF FAQ Knowledge Bot for answering repeat questions from uploaded documents. Tailored topic: Education Planning Evidence Review Simple RAG - Beginner Custom 5.'
USER_PERSONA = 'Support specialist'
STARTER_QUESTIONS = ['What should I know first about Education Planning Evidence Review Simple RAG - Beginner Custom 5?', 'Which source supports the next action for pdf faq knowledge bot?', 'Create a support specialist checklist for this case.']
WORKFLOW_STEPS = ['Receive question', 'Search FAQ documents', 'Cite the matching answer', 'Suggest next step']
BUSINESS_RULES = ['Answer only from retrieved context', 'Show source names', 'Ask for clarification when confidence is low']
TOOL_CATALOG = [{'name': 'document_search', 'description': 'Find FAQ passages'}, {'name': 'clarifier', 'description': 'Ask one focused follow-up'}]
