import pandas as pd
from openpyxl import Workbook

# Define modules and their respective questions
modules = {
    'BizX': [
        {
            'Question':
            'What is the primary use of BizX in SAP SuccessFactors?',
            'Option 1': 'Employee Central',
            'Option 2': 'Performance Management',
            'Option 3': 'Learning Management',
            'Option 4': 'Core HR',
            'Answer': 'Performance Management'
        },
        {
            'Question': 'What is a key feature of the BizX suite?',
            'Option 1': 'Reporting and Analytics',
            'Option 2': 'System Configuration',
            'Option 3': 'Data Replication',
            'Option 4': 'Workflow Management',
            'Answer': 'Reporting and Analytics'
        },
        {
            'Question':
            'How can goals be cascaded down the organization in BizX?',
            'Option 1': 'Manual assignment',
            'Option 2': 'Top-down cascading',
            'Option 3': 'Manager-employee collaboration',
            'Option 4': 'Pre-defined templates',
            'Answer': 'Manager-employee collaboration'
        },
        {
            'Question':
            'What type of feedback can be provided during performance reviews in BizX?',
            'Option 1': 'Textual only',
            'Option 2': 'Ratings only',
            'Option 3': 'Textual and ratings',
            'Option 4': 'Pre-defined comments',
            'Answer': 'Textual and ratings'
        },
        {
            'Question': 'What is the purpose of the Goal Library in BizX?',
            'Option 1': 'Store historical goal data',
            'Option 2': 'Share best practices',
            'Option 3': 'Create reusable goal templates',
            'Option 4': 'Track individual goal progress',
            'Answer': 'Create reusable goal templates'
        },
        {
            'Question':
            'How can managers provide real-time feedback to employees in BizX?',
            'Option 1': 'Email notifications',
            'Option 2': 'In-app messaging',
            'Option 3': 'Scheduled check-ins',
            'Option 4': 'All of the above',
            'Answer': 'All of the above'
        },
        {
            'Question': 'What is the role of the Goal Owner in BizX?',
            'Option 1': 'Sets goals for the entire organization',
            'Option 2': 'Monitors goal progress',
            'Option 3': 'Provides feedback on goal performance',
            'Option 4': 'All of the above',
            'Answer': 'All of the above'
        },
        {
            'Question':
            'How can employees track their own goal progress in BizX?',
            'Option 1': 'Goal dashboard',
            'Option 2': 'Performance summary report',
            'Option 3': 'Manager feedback',
            'Option 4': 'All of the above',
            'Answer': 'Goal dashboard'
        },
        {
            'Question':
            'What is the purpose of the Calibration feature in BizX?',
            'Option 1': 'Ensure consistent performance ratings',
            'Option 2': 'Automate performance reviews',
            'Option 3': 'Generate performance reports',
            'Option 4': 'Track employee development plans',
            'Answer': 'Ensure consistent performance ratings'
        },
        {
            'Question':
            'How can managers identify high-potential employees in BizX?',
            'Option 1': 'Performance ratings',
            'Option 2': 'Goal achievement',
            'Option 3': 'Talent pools',
            'Option 4': 'All of the above',
            'Answer': 'All of the above'
        },
        {
            'Question':
            'What is the purpose of the Succession Planning feature in BizX?',
            'Option 1': 'Identify potential successors for key roles',
            'Option 2': 'Track employee development plans',
            'Option 3': 'Manage talent pools',
            'Option 4': 'All of the above',
            'Answer': 'All of the above'
        },
        {
            'Question':
            'What is the role of the Compensation Advisor in BizX?',
            'Option 1': 'Administers compensation plans',
            'Option 2': 'Conducts compensation reviews',
            'Option 3': 'Provides compensation recommendations',
            'Option 4': 'All of the above',
            'Answer': 'All of the above'
        },
        {
            'Question':
            'How can employees access their compensation information in BizX?',
            'Option 1': 'Employee self-service portal',
            'Option 2': 'Manager approval',
            'Option 3': 'HR representative',
            'Option 4': 'All of the above',
            'Answer': 'Employee self-service portal'
        },
        {
            'Question':
            'What is the purpose of the Job Profile feature in BizX?',
            'Option 1': 'Define job roles and responsibilities',
            'Option 2': 'Track employee performance',
            'Option 3': 'Manage talent pools',
            'Option 4': 'All of the above',
            'Answer': 'Define job roles and responsibilities'
        },
        {
            'Question':
            'How can organizations ensure data privacy and security in BizX?',
            'Option 1': 'Role-based access control',
            'Option 2': 'Data encryption',
            'Option 3': 'Regular security audits',
            'Option 4': 'All of the above',
            'Answer': 'All of the above'
        },
        {
            'Question':
            'What is the purpose of the Integration Center in BizX?',
            'Option 1': 'Integrate with other SAP SuccessFactors modules',
            'Option 2': 'Integrate with third-party applications',
            'Option 3': 'Automate workflows',
            'Option 4': 'All of the above',
            'Answer': 'All of the above'
        },
        {
            'Question':
            'How can organizations customize the BizX interface to meet their specific needs?',
            'Option 1': 'Configuration settings',
            'Option 2': 'Custom fields and objects',
            'Option 3': 'Workflow customization',
            'Option 4': 'All of the above',
            'Answer': 'All of the above'
        },
        {
            'Question':
            'What is the purpose of the Analytics feature in BizX?',
            'Option 1': 'Generate performance reports',
            'Option 2': 'Track key performance indicators (KPIs)',
            'Option 3': 'Identify trends and insights',
            'Option 4': 'All of the above',
            'Answer': 'All of the above'
        },
        {
            'Question':
            'How can organizations ensure data accuracy and consistency in BizX?',
            'Option 1': 'Data validation rules',
            'Option 2': 'Data quality checks',
            'Option 3': 'Data cleansing processes',
            'Option 4': 'All of the above',
            'Answer': 'All of the above'
        },
        {
            'Question':
            'How can organizations measure the effectiveness of their performance management processes in BizX?',
            'Option 1': 'Employee satisfaction surveys',
            'Option 2': 'Performance metrics',
            'Option 3': 'Business outcomes',
            'Option 4': 'All of the above',
            'Answer': 'All of the above'
        },
    ],
    'Mobile': [
        {
            'Question':
            'Which platform does the SAP SuccessFactors mobile app support?',
            'Option 1': 'iOS only',
            'Option 2': 'Android only',
            'Option 3': 'iOS and Android',
            'Option 4': 'Windows only',
            'Answer': 'iOS and Android'
        },
        {
            'Question':
            'How can users access SAP SuccessFactors modules via mobile devices?',
            'Option 1': 'Web App only',
            'Option 2': 'Mobile Native App',
            'Option 3': 'Desktop Mode',
            'Option 4': 'API Integration',
            'Answer': 'Mobile Native App'
        },
        {
            'Question':
            'What features are available for offline access in the mobile app?',
            'Option 1': 'No offline capabilities',
            'Option 2': 'Limited data viewing',
            'Option 3': 'Full functionality',
            'Option 4': 'Time-sensitive tasks',
            'Answer': 'Limited data viewing'
        },
        {
            'Question':
            'Can users submit leave requests through the mobile app?',
            'Option 1': 'No, leave requests require a desktop computer',
            'Option 2': 'Yes, for pre-approved absences only',
            'Option 3': 'Yes, for all leave types',
            'Option 4': 'Leave requests require manager approval via the app',
            'Answer': 'Yes, for all leave types'
        },
        {
            'Question':
            'How can users receive notifications from SAP SuccessFactors on their mobile devices?',
            'Option 1': 'Email only',
            'Option 2': 'Push notifications',
            'Option 3': 'SMS messages',
            'Option 4': 'All of the above',
            'Answer': 'Push notifications'
        },
        {
            'Question':
            'Can users access performance reviews and feedback through the mobile app?',
            'Option 1': 'No, performance reviews require a desktop computer',
            'Option 2': 'Yes, for viewing only',
            'Option 3': 'Yes, for viewing and providing feedback',
            'Option 4': 'Yes, for all performance management activities',
            'Answer': 'Yes, for viewing and providing feedback'
        },
        {
            'Question':
            'How can users access their time-off balances and request time off through the mobile app?',
            'Option 1': 'Employee self-service portal',
            'Option 2': 'Manager approval',
            'Option 3': 'HR representative',
            'Option 4': 'All of the above',
            'Answer': 'Mobile app'
        },
        {
            'Question':
            'Can users access learning content and complete courses through the mobile app?',
            'Option 1': 'No, learning activities require a desktop computer',
            'Option 2': 'Yes, for viewing content only',
            'Option 3': 'Yes, for completing courses and quizzes',
            'Option 4': 'Yes, for all learning activities',
            'Answer': 'Yes , for completing courses and quizzes'
        },
        {
            'Question':
            'How can users access their pay stubs and tax information through the mobile app?',
            'Option 1': 'Employee self-service portal',
            'Option 2': 'Manager approval',
            'Option 3': 'HR representative',
            'Option 4': 'Mobile app',
            'Answer': 'Mobile app'
        },
        {
            'Question':
            'Can users receive alerts for important deadlines and reminders through the mobile app?',
            'Option 1': 'No, alerts are only sent via email',
            'Option 2': 'Yes, for selected notifications',
            'Option 3': 'Yes, for all important notifications',
            'Option 4': 'Alerts are not supported on mobile devices',
            'Answer': 'Yes, for all important notifications'
        },
        {
            'Question':
            'How can users access their personal information and make updates through the mobile app?',
            'Option 1': 'Employee self-service portal',
            'Option 2': 'Manager approval',
            'Option 3': 'HR representative',
            'Option 4': 'Mobile app',
            'Answer': 'Mobile app'
        },
        {
            'Question':
            'Can users participate in surveys and polls through the mobile app?',
            'Option 1': 'No, surveys and polls require a desktop computer',
            'Option 2': 'Yes, for viewing results only',
            'Option 3': 'Yes, for participating and submitting responses',
            'Option 4':
            'Surveys and polls are not supported on mobile devices',
            'Answer': 'Yes, for participating and submitting responses'
        },
        {
            'Question':
            'How can users access company news and announcements through the mobile app?',
            'Option 1': 'Company intranet',
            'Option 2': 'Email notifications',
            'Option 3': 'Mobile app',
            'Option 4': 'All of the above',
            'Answer': 'Mobile app'
        },
        {
            'Question':
            'Can users access organizational charts and employee directories through the mobile app?',
            'Option 1':
            'No, organizational charts are only available on desktop',
            'Option 2': 'Yes, for viewing only',
            'Option 3': 'Yes, for viewing and searching',
            'Option 4':
            'Organizational charts are not supported on mobile devices',
            'Answer': 'Yes, for viewing and searching'
        },
        {
            'Question':
            'How can users receive emergency alerts and notifications through the mobile app?',
            'Option 1': 'Email only',
            'Option 2': 'Push notifications',
            'Option 3': 'SMS messages',
            'Option 4': 'All of the above',
            'Answer': 'Push notifications and SMS messages'
        },
        {
            'Question':
            'Can users access their expense reports and submit expense claims through the mobile app?',
            'Option 1': 'No, expense management requires a desktop computer',
            'Option 2': 'Yes, for viewing only',
            'Option 3': 'Yes, for submitting expense claims and approvals',
            'Option 4':
            'Expense management is not supported on mobile devices',
            'Answer': 'Yes, for submitting expense claims and approvals'
        },
        {
            'Question':
            'How can users access their training and development plans through the mobile app?',
            'Option 1': 'Employee self-service portal',
            'Option 2': 'Manager approval',
            'Option 3': 'HR representative',
            'Option 4': 'Mobile app',
            'Answer': 'Mobile app'
        },
        {
            'Question':
            'Can users participate in virtual meetings and webinars through the mobile app?',
            'Option 1': 'No, virtual meetings require a desktop computer',
            'Option 2': 'Yes, for audio-only participation',
            'Option 3': 'Yes, for video and audio participation',
            'Option 4': 'Virtual meetings are not supported on mobile devices',
            'Answer': 'Yes, for video and audio participation'
        },
        {
            'Question':
            'How can users access their work schedules and shift patterns through the mobile app?',
            'Option 1': 'Employee self-service portal',
            'Option 2': 'Manager approval',
            'Option 3': 'HR representative',
            'Option 4': 'Mobile app',
            'Answer': 'Mobile app'
        },
        {
            'Question':
            'Can users access their payroll information and payslips through the mobile app?',
            'Option 1': 'No, payroll information is only available on desktop',
            'Option 2': 'Yes, for viewing only',
            'Option 3': 'Yes, for viewing and downloading',
            'Option 4':
            'Payroll information is not supported on mobile devices',
            'Answer': 'Yes, for viewing and downloading'
        },
        {
            'Question':
            'How can users access company policies and procedures through the mobile app?',
            'Option 1': 'Company intranet',
            'Option 2': 'Email notifications',
            'Option 3': 'Mobile app',
            'Option 4': 'All of the above',
            'Answer': 'Mobile app'
        },
    ],
    'Data Services': [
        {
            'Question':
            'What is the primary use of Data Services in SAP SuccessFactors?',
            'Option 1': 'Data Reporting',
            'Option 2': 'Integration Platform',
            'Option 3': 'Learning Management',
            'Option 4': 'Core HR',
            'Answer': 'Integration Platform'
        },
        {
            'Question':
            'Which service type does Data Services offer for integration?',
            'Option 1': 'ETL Service',
            'Option 2': 'On-Premise Service',
            'Option 3': 'iPaaS (Integration Platform as a Service)',
            'Option 4': 'Cloud Security Service',
            'Answer': 'iPaaS (Integration Platform as a Service)'
        },
        {
            'Question': 'What is a Process in Data Services?',
            'Option 1': 'A sequence of steps to automate a task',
            'Option 2': 'A data source',
            'Option 3': 'A target system',
            'Option 4': 'A connector',
            'Answer': 'A sequence of steps to automate a task'
        },
        {
            'Question':
            'What is a Connector in Data Services?',
            'Option 1':
            'A software component that allows Data Services to interact with other systems',
            'Option 2':
            'A data transformation step',
            'Option 3':
            'A security mechanism',
            'Option 4':
            'A monitoring tool',
            'Answer':
            'A software component that allows Data Services to interact with other systems'
        },
        {
            'Question': 'What is a Shape in Data Services?',
            'Option 1': 'A graphical representation of a process step',
            'Option 2': 'A data format',
            'Option 3': 'A security setting',
            'Option 4': 'A performance metric',
            'Answer': 'A graphical representation of a process step'
        },
        {
            'Question': 'What is a Profile in Data Services?',
            'Option 1':
            'A set of properties that define a connection to a system',
            'Option 2': 'A user account',
            'Option 3': 'A process variable',
            'Option 4': 'A document type',
            'Answer':
            'A set of properties that define a connection to a system'
        },
        {
            'Question': 'What is the purpose of the Data Services Agent?',
            'Option 1': 'To execute processes',
            'Option 2': 'To store data',
            'Option 3': 'To monitor system performance',
            'Option 4': 'To provide user interface',
            'Answer': 'To execute processes'
        },
        {
            'Question':
            'What is the difference between a synchronous and asynchronous process in Data Services?',
            'Option 1':
            'Synchronous processes wait for a response, asynchronous processes do not',
            'Option 2':
            'Synchronous processes are faster, asynchronous processes are slower',
            'Option 3':
            'Synchronous processes are more reliable, asynchronous processes are less reliable',
            'Option 4':
            'Synchronous processes are simpler, asynchronous processes are more complex',
            'Answer':
            'Synchronous processes wait for a response, asynchronous processes do not'
        },
        {
            'Question': 'What is the purpose of the Data Services Repository?',
            'Option 1': 'To store metadata about data sources and targets',
            'Option 2': 'To store data transformations and mappings',
            'Option 3': 'To store data quality rules',
            'Option 4': 'All of the above',
            'Answer': 'All of the above'
        },
        {
            'Question':
            'How can performance issues be identified and resolved in Data Services?',
            'Option 1': 'Performance monitoring tools',
            'Option 2': 'Performance tuning techniques',
            'Option 3': 'Performance optimization strategies',
            'Option 4': 'All of the above',
            'Answer': 'All of the above'
        },
        {
            'Question': 'What is the purpose of the Data Services Job Server?',
            'Option 1': 'To schedule and execute data jobs',
            'Option 2': 'To monitor data job execution',
            'Option 3': 'To handle errors and exceptions',
            'Option 4': 'All of the above',
            'Answer': 'All of the above'
        },
        {
            'Question':
            'How can data consistency be maintained across different systems using Data Services?',
            'Option 1': 'Data synchronization',
            'Option 2': 'Data replication',
            'Option 3': 'Data quality rules',
            'Option 4': 'All of the above',
            'Answer': 'All of the above'
        },
        {
            'Question':
            'What is the purpose of the Data Services Change Data Capture (CDC) feature?',
            'Option 1': 'Capture changes to data sources',
            'Option 2': 'Apply changes to target systems',
            'Option 3': 'Optimize data integration performance',
            'Option 4': 'All of the above',
            'Answer': 'All of the above'
        },
    ],
    'Boomi': [
        {
            'Question':
            'What is Boomi primarily used for in the context of SAP SuccessFactors?',
            'Option 1': 'Data Reporting',
            'Option 2': 'Integration Platform',
            'Option 3': 'Learning Management',
            'Option 4': 'Core HR',
            'Answer': 'Integration Platform'
        },
        {
            'Question': 'Which service type does Boomi offer for integration?',
            'Option 1': 'ETL Service',
            'Option 2': 'On-Premise Service',
            'Option 3': 'iPaaS (Integration Platform as a Service)',
            'Option 4': 'Cloud Security Service',
            'Answer': 'iPaaS (Integration Platform as a Service)'
        },
        {
            'Question': 'What is a Process in Boomi?',
            'Option 1': 'A sequence of steps to automate a task',
            'Option 2': 'A data source',
            'Option 3': 'A target system',
            'Option 4': 'A connector',
            'Answer': 'A sequence of steps to automate a task'
        },
        {
            'Question':
            'What is a Connector in Boomi?',
            'Option 1':
            'A software component that allows Boomi to interact with other systems',
            'Option 2':
            'A data transformation step',
            'Option 3':
            'A security mechanism',
            'Option 4':
            'A monitoring tool',
            'Answer':
            'A software component that allows Boomi to interact with other systems'
        },
        {
            'Question': 'What is a Shape in Boomi?',
            'Option 1': 'A graphical representation of a process step',
            'Option 2': 'A data format',
            'Option 3': 'A security setting',
            'Option 4': 'A performance metric',
            'Answer': 'A graphical representation of a process step'
        },
        {
            'Question': 'What is a Profile in Boomi?',
            'Option 1':
            'A set of properties that define a connection to a system',
            'Option 2': 'A user account',
            'Option 3': 'A process variable',
            'Option 4': 'A document type',
            'Answer':
            'A set of properties that define a connection to a system'
        },
        {
            'Question': 'What is the purpose of the Boomi Atom?',
            'Option 1': 'To execute processes',
            'Option 2': 'To store data',
            'Option 3': 'To monitor system performance',
            'Option 4': 'To provide user interface',
            'Answer': 'To execute processes'
        },
        {
            'Question':
            'What is the difference between a synchronous and asynchronous process in Boomi?',
            'Option 1':
            'Synchronous processes wait for a response, asynchronous processes do not',
            'Option 2':
            'Synchronous processes are faster, asynchronous processes are slower',
            'Option 3':
            'Synchronous processes are more reliable, asynchronous processes are less reliable',
            'Option 4':
            'Synchronous processes are simpler, asynchronous processes are more complex',
            'Answer':
            'Synchronous processes wait for a response, asynchronous processes do not'
        },
        {
            'Question': 'What is the purpose of the Boomi Community?',
            'Option 1': 'To provide technical support',
            'Option 2': 'To share best practices and knowledge',
            'Option 3': 'To purchase Boomi licenses',
            'Option 4': 'To access training materials',
            'Answer': 'To share best practices and knowledge'
        },
        {
            'Question':
            'What is the purpose of the Boomi API Management feature?',
            'Option 1': 'To manage API security',
            'Option 2': 'To design and publish APIs',
            'Option 3': 'To consume APIs from external systems',
            'Option 4': 'All of the above',
            'Answer': 'All of the above'
        },
        {
            'Question': 'What is the purpose of the Boomi Master Data Hub?',
            'Option 1': 'To manage master data across multiple systems',
            'Option 2': 'To synchronize data between systems',
            'Option 3': 'To clean and transform data',
            'Option 4': 'All of the above',
            'Answer': 'All of the above'
        },
        {
            'Question':
            'What is the purpose of the Boomi Process Reporting feature?',
            'Option 1': 'To monitor process performance',
            'Option 2': 'To identify bottlenecks',
            'Option 3': 'To analyze process errors',
            'Option 4': 'All of the above',
            'Answer': 'All of the above'
        },
        {
            'Question':
            'What is the purpose of the Boomi Data Quality feature?',
            'Option 1': 'To ensure data accuracy and consistency',
            'Option 2': 'To clean and transform data',
            'Option 3': 'To validate data against business rules',
            'Option 4': 'All of the above',
            'Answer': 'All of the above'
        },
        {
            'Question':
            'What is the purpose of the Boomi Cloud Connect feature?',
            'Option 1': 'To connect to cloud-based applications',
            'Option 2': 'To secure cloud-based integrations',
            'Option 3': 'To optimize cloud-based integrations',
            'Option 4': 'All of the above',
            'Answer': 'All of the above'
        },
        {
            'Question':
            'What is the purpose of the Boomi Operational Insights feature?',
            'Option 1': 'To monitor system health',
            'Option 2': 'To identify performance issues',
            'Option 3': 'To troubleshoot integration problems',
            'Option 4': 'All of the above',
            'Answer': 'All of the above'
        },
        {
            'Question': 'What is the purpose of the Boomi Integration Pack?',
            'Option 1': 'A pre-built integration template',
            'Option 2': 'A security setting',
            'Option 3': 'A performance optimization technique',
            'Option 4': 'A data transformation tool',
            'Answer': 'A pre-built integration template'
        },
    ]
}
