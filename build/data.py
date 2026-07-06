# -*- coding: utf-8 -*-
"""Content data for all 10 case studies, the projects grid, and shared copy.

Images and external links are hotlinked from the real, currently-live
javidesignlabs.com (Framer) CDN — these are Javi's own published assets.
"""

PROFILE = {
    # Change BASE_URL to "https://javidesignlabs.com" when you point your custom domain here
    "base_url": "https://javidesignlabs.github.io/myporfolio",
    "avatar_hero": "https://framerusercontent.com/images/Bv3kCGt7CVS9r8dtdbxDJa5hHY.jpeg",
    "avatar_about": "https://framerusercontent.com/images/UdHGJxJMIvCQPbsnF3793NhTyzw.jpg",
    "avatar_footer": "https://framerusercontent.com/images/P6TXEOXYaHG6z5IeGjc5TZIwFXM.jpg",
    "hero_graphic": "https://framerusercontent.com/images/EMwh8pAhkhVzPNPRsoohSuFfQ.jpeg",
    "linkedin": "https://www.linkedin.com/in/jdelacruztel/?locale=en_US",
    "x": "https://x.com/bynneh",
    "cal": "https://cal.com/jdlct81",
    "resume": "https://www.dropbox.com/scl/fi/cnsw0qy0hy00ilttjgrl9/Resume_2025.pdf?rlkey=vtqt9nx7dcgjkg0xly9ipgd5j&st=5209p04e&dl=0",
    "mailto": "javierdelacruztellez@gmail.com",
    "email_display": "hello@javidesignlabs.com",
}

NAV = [
    ("Projects", "projects.html"),
    ("About & Contact", "about.html"),
]

CLIENTS = ["MotoGP", "Bolttech", "BASF", "Desigual", "Inari.io", "Bershka", "WorldSBK", "Gluecharm"]

# Real, sourced metrics pulled from the case studies / career history
PROOF = [
    ("45", "%", "resource-management gain from the Bolttech supply-chain SaaS", "Bolttech · 2021–23"),
    ("23", "%", "conversion lift after redesigning Desigual's product card", "Desigual · 2013–16"),
    ("17", "%", "retention increase from the MotoGP renewal redesign", "Dorna Sports · 2016–21"),
    ("15", "%", "faster access times across Bolttech partner portals", "Bolttech · 2021–23"),
]

CAPABILITIES = [
    "Design systems & tokens",
    "Component libraries & docs",
    "UX standards & guidelines",
    "Product & UX/UI design",
    "Design-to-dev workflows",
    "Cross-team adoption & DesignOps",
]

PROJECTS = [
    {
        "slug": "saas-supply-chain",
        "cover_img": "https://framerusercontent.com/images/BpCaafId9OJ1JASCegLAJX3k.jpg",
        "tag": "SaaS",
        "title": "SaaS Supply Chain Service",
        "subtitle": "Optimizing Repair Center Management: A User-Centered Approach to Streamline Operations and Enhance Customer Experience",
        "role": "UI/UX design",
        "category": "SaaS",
        "company": "Bolttech",
        "website": 'https://backmarket.bolttech.eu/#/',
        "illustration": "warehouse",
        "intro": [
            "In 2022/23, I led the design of a SaaS solution for supply chain management, focusing on optimizing the interaction between repair centers, the supply chain team, and customer service.",
            "Manual processes in managing repair center information caused inefficiencies and errors, negatively impacting customer service quality and operational efficiency.",
        ],
        "context": "The Supply Chain (SC) team manually managed all their operations, relying heavily on emails, phone calls, and weekly updates to an Excel file. This process was not only inefficient and prone to errors but also led to duplicated work. On the other hand, the Customer Service (CS) team faced challenges when searching for the nearest repair centers for customers, as there was no integration within the SaaS platform.",
        "problem": [
            "The lack of automation and centralized information created inefficiencies, errors, and delays in communication between the Supply Chain, Customer Service, and Repair Center teams.",
        ],
        "objective": "Design and implement a solution that would automate workflows, reduce operational time, and centralize information into an integrated system accessible to all teams.",
        "responsibilities": [
            "Create a detailed roadmap to deliver the first MVP.",
            "Conduct in-depth research with the involved teams (SC, CS, and Repair Centers).",
            "Design a user-centered solution to address the main pain points.",
        ],
        "research": [
            ("Interviews with the Supply Chain (SC) team", "Identified that the manual process of updating the Excel file was error-prone and time-consuming."),
            ("Shadowing the Customer Service (CS) team", "Observed that the lack of integration in the SaaS platform caused delays in searching for repair center information."),
            ("Interviews with Repair Centers", "Discovered there was no standardized flow for communicating changes in pricing, schedules, and availability."),
        ],
        "design_blocks": [
            ("For the Supply Chain (SC) team", "I designed a SaaS system that automated data import from the Excel file, enabling critical actions such as opening/closing stores, editing information, and selecting the best options based on updated pricing."),
            ("For Repair Centers", "I created a connected client within the SaaS system, allowing centers to upload a weekly JSON file with updated information."),
            ("For the Customer Service (CS) team", "I integrated a new feature into the SaaS platform that allowed CS to search for the nearest repair centers directly within the system, eliminating reliance on the external Excel file."),
        ],
        "impact": [
            ("40% increase in operational efficiency", "Eliminating the chaos of manual data entry."),
            ("Significant reduction in search times", "For the Customer Service team, improving customer interactions."),
            ("Scalable and modular system", "Ready for continuous improvements and optimized loading times."),
        ],
        "qualitative": [
            "Greater autonomy for Repair Centers, while maintaining full connectivity with the Supply Chain team.",
            "Improved collaboration between teams, eliminating communication inconsistencies.",
        ],
        "learnings": [
            "Interdisciplinary collaboration was essential to gain a comprehensive understanding of the problem and design a versatile solution.",
            "Using Bolttech's design system ensured a consistent and functional user experience.",
            "The system's scalability highlighted the importance of building solutions that evolve with business and user needs.",
        ],
    },
    {
        "slug": "bolttech-design-system",
        "cover_img": "https://framerusercontent.com/images/frKhVknw8YUYEnhirTjNLuXz3e4.png",
        "tag": "Design system",
        "title": "Establishing Bolttech's Design System: From Concept to Implementation",
        "subtitle": "Crafting a Cohesive and Scalable Design Framework for Enhanced User Experience",
        "role": "UI/UX design",
        "category": "Design system",
        "company": "Bolttech",
        "website": 'https://bolttech.io/distribution-engine/',
        "illustration": "design-system",
        "intro": [
            "I collaborated with Bolttech's design team to develop a comprehensive design system from the ground up.",
            "This initiative involved creating standardized components, thorough documentation, and design tokens to ensure consistency and efficiency across the company's digital products.",
        ],
        "context": "Bolttech lacked a unified design system, which led to inconsistencies across its digital platforms. This lack of standardization created challenges in maintaining a cohesive user experience and slowed down both design and development processes.",
        "problem": [
            "Inconsistent design components and interactions across platforms.",
            "Lack of a centralized framework for design and development collaboration.",
            "Difficulty in scaling and maintaining consistency as the company grew.",
        ],
        "objective": "Create a unified design system that would standardize components, improve collaboration between design and development teams, and ensure consistency across all digital products.",
        "responsibilities": [
            "Design components aligned with Bolttech's brand guidelines.",
            "Document the design system using tools like Zeroheight.",
            "Create design tokens in Figma to ensure seamless integration with development workflows.",
        ],
        "research": [
            ("Research and planning", "Analyzed existing design inconsistencies and identified key areas for improvement, and collaborated with stakeholders to define the design system's scope and goals."),
        ],
        "design_blocks": [
            ("Design and development", "Designed reusable components and interactions aligned with Bolttech's brand guidelines, used Figma to create design tokens ensuring consistency across all platforms, and documented the design system in Zeroheight, making it accessible to both design and development teams."),
            ("Implementation", "Worked closely with developers to integrate the design system into Bolttech's digital products, and conducted training sessions for designers and developers to ensure proper adoption of the new system."),
        ],
        "impact": [
            ("Streamlined workflows", "The design system reduced the time spent on recreating components and resolving inconsistencies."),
            ("Enhanced user experience", "Standardized components and interactions improved the overall usability and consistency of Bolttech's digital products."),
            ("Scalability", "The design system provided a solid foundation for future growth, enabling faster and more efficient development of new features and products."),
        ],
        "qualitative": [],
        "learnings": [
            "A unified design system is essential for maintaining consistency and scalability in a growing company.",
            "Collaboration between design and development teams is crucial for successful implementation.",
            "Tools like Figma and Zeroheight are invaluable for creating and documenting design systems.",
        ],
    },
    {
        "slug": "partner-portals",
        "cover_img": "https://framerusercontent.com/images/wvmDSEbjdRvEPLWhtyWIUhJrjnM.jpg",
        "tag": "Desktop and Mobile",
        "title": "Enhancing Partner Portals: A User-Centered Redesign for Bolttech",
        "subtitle": "Optimizing B2B and B2C Interfaces to Improve User Experience and Operational Efficiency",
        "role": "UI/UX design",
        "category": "Desktop and Mobile",
        "company": "Bolttech",
        "website": 'https://fnaccare.ch/#/',
        "illustration": "portal",
        "intro": [
            "Between 2021 and 2023, I led the redesign of partner portals for Bolttech, focusing on clients like Fnac and Orange.",
            "Through comprehensive user research and iterative design processes, we achieved a 15% improvement in access time and enhanced task completion efficiency, resulting in a more intuitive and streamlined user experience.",
        ],
        "context": "Bolttech's partner portals were facing usability challenges, which led to inefficiencies in user interactions. These issues created frustration for users and hindered their ability to perform tasks effectively.",
        "problem": [
            "Poor usability and inefficient workflows.",
            "Long access times and difficulty in completing tasks.",
            "Lack of a user-centered design approach.",
        ],
        "objective": "Redesign the partner portals to improve usability, streamline workflows, and enhance the overall user experience.",
        "responsibilities": [
            "Conduct user research to identify pain points and areas for improvement.",
            "Collaborate with development teams to investigate and enhance the existing codebase.",
            "Design and implement a user-centered solution.",
        ],
        "research": [
            ("User interviews and workflow analyses", "Identified key pain points and usability issues, and gathered insights from stakeholders to understand their needs and expectations."),
        ],
        "design_blocks": [
            ("Design and development", "Created detailed wireframes to visualize the redesigned portal, engaged in multiple stakeholder reviews to refine the design and ensure alignment with business goals, and collaborated closely with development teams during sprints to implement the improvements."),
            ("Implementation", "Rolled out the redesigned portal, focusing on improving access times and streamlining task performance, and conducted usability testing to validate the changes and gather feedback for further iterations."),
        ],
        "impact": [
            ("15% improvement in access times", "Making the portal faster and more responsive."),
            ("Streamlined user task performance", "Reducing the time and effort required to complete tasks."),
            ("Enhanced user experience", "Leading to higher satisfaction among partners."),
        ],
        "qualitative": [
            "Increased operational efficiency for Bolttech's partners, contributing to better overall performance.",
        ],
        "learnings": [
            "User research is critical for identifying pain points and designing effective solutions.",
            "Collaboration between design and development teams ensures smoother implementation.",
            "A user-centered approach leads to tangible improvements in usability and efficiency.",
        ],
    },
    {
        "slug": "saas-process-modeling",
        "cover_img": "https://framerusercontent.com/images/LdMym2jStT80OZnoQwnKx2fViQ.png",
        "tag": "SaaS",
        "title": "SaaS Process Modeling: Transforming ideas into technical specifications",
        "subtitle": "Leveraging AI to bridge the gap between concept and implementation",
        "role": "UI/UX design",
        "category": "SaaS",
        "company": "Gluecharm",
        "website": 'https://www.gluecharm.com',
        "illustration": "gluecharm",
        "intro": [
            "I led the design of Gluecharm, an AI-driven Technical Analyst tool that converts product or feature concepts into detailed technical specifications.",
            "This initiative aimed to enhance collaboration between product owners and development teams, streamlining the review process and accelerating development cycles.",
        ],
        "context": "Gluecharm was a side project developed between 2022 and 2023, inspired by the rise of generative AI and the challenges faced by technical teams in creating high-level documentation for software development. There was a lack of standardization in the process, leading to inefficiencies and frustration.",
        "problem": [
            "Excessive time spent on creating and updating technical documentation.",
            "Lack of a standardized structure for documents.",
            "Difficulty for non-technical users to participate in the documentation process.",
        ],
        "objective": "Develop a tool that simplifies technical documentation processes, automates repetitive tasks, and provides an efficient way of structuring and generating documentation, regardless of the user's experience level.",
        "responsibilities": [
            "Collaborate with the product team to define and develop an MVP.",
            "Conduct user research to identify pain points and needs.",
            "Design and implement a user-friendly, AI-powered documentation tool.",
        ],
        "research": [
            ("User interviews and focus group sessions", "Held with both technical and non-technical users to understand their challenges."),
            ("Shadowing sessions", "Performed with key roles (product owners, analysts) to observe their interaction with documentation tools and identify pain points."),
            ("Three main areas of focus", "Identified: structured report generation, task automation, and improved data analysis processes."),
        ],
        "design_blocks": [
            ("Design and development", "Created wireframes to detail user flows and ensure alignment with user needs, designed a user-friendly interface that allowed users to interact with AI to generate technical documentation by answering three key questions, and implemented a design system based on the Tailwind library to ensure scalability and consistency."),
            ("Developed features such as", "Suggested product names, identification of problems and proposed solutions, user definitions with customizable preferences, use cases, scenarios, technical diagrams, and data models, and conversion of use cases into user stories with AI assistance."),
            ("Implementation", "Built a stable, scalable platform that automated key tasks and reduced the time spent on documentation, and conducted usability testing to validate the tool's effectiveness and gather feedback for improvements."),
        ],
        "impact": [
            ("Reduced time and effort", "Spent on technical documentation through automation and AI assistance."),
            ("Improved accessibility", "For non-technical users, enabling them to participate in the documentation and maintain technical documents."),
            ("Standardized documentation structure", "Making it easier for teams to create and maintain technical documents."),
        ],
        "qualitative": [
            "Scalable and user-friendly platform that met the needs of both technical and non-technical users.",
        ],
        "learnings": [
            "Interdisciplinary collaboration was essential for understanding diverse user needs and designing a versatile product.",
            "AI-driven tools can significantly simplify complex processes, making them more efficient and accessible.",
        ],
    },
    {
        "slug": "payment-renewal",
        "cover_img": "https://framerusercontent.com/images/cD4x3P1lTyys2SAT5dwR7XDFHc.jpg",
        "tag": "UX UI",
        "title": "Redesigning Payment and Renewal Experiences",
        "subtitle": "Optimizing User Journeys for Better Conversion Rates and Customer Satisfaction",
        "role": "UI/UX design",
        "category": "UX UI",
        "company": "Dorna Sport",
        "website": None,
        "illustration": "payment",
        "intro": [
            "In 2019, the payment and product renewal processes faced significant challenges, leading to user frustration and decreased retention rates.",
            "By conducting in-depth research and leveraging user insights, I designed and implemented solutions that streamlined workflows, improved usability, and enhanced the overall user experience.",
        ],
        "context": "In 2019, users were experiencing confusion and dissatisfaction with the payment and automatic product renewal processes. This led to a poor user experience and potentially impacted customer retention and conversion rates.",
        "problem": [
            "Users confused by the payment and renewal processes.",
            "Lack of clarity in system status and error recovery options.",
            "Low customer satisfaction and potential loss of revenue due to user frustration.",
        ],
        "objective": "Redesign the payment and automatic renewal processes to improve user clarity, satisfaction, and conversion rates.",
        "responsibilities": [
            "Conduct a comprehensive assessment of user behavior and pain points.",
            "Design optimized workflows and high-fidelity prototypes.",
            "Validate the designs through usability testing and implement improvements.",
        ],
        "research": [
            ("Event log analysis", "Conducted to identify behavioral patterns and areas of confusion."),
            ("Customer satisfaction surveys", "Distributed to gather feedback on the existing processes."),
            ("Qualitative interviews", "Performed to gain deeper insights into user pain points and needs."),
            ("Representative user personas", "Created to guide the design process and ensure a user-centered approach."),
        ],
        "design_blocks": [
            ("Design", "Designed optimized workflows to simplify the payment and renewal processes, and developed high-fidelity prototypes using Sketch, incorporating user-centered design principles such as system status visibility (ensuring users were always aware of their current status in the process) and error recovery capabilities (providing clear options for users to correct mistakes or cancel actions)."),
            ("Implementation", "Collaborated with development teams to implement the redesigned workflows and interfaces, and monitored user behavior and satisfaction post-launch to ensure the changes had the desired impact."),
        ],
        "impact": [
            ("Improved user clarity", "The redesigned processes reduced confusion and made it easier for users to understand and complete payment and renewal steps."),
            ("Increased conversion rates", "The streamlined workflows led to measurable improvements in conversion rates."),
            ("Higher user satisfaction", "Usability testing and post-launch feedback indicated a significant increase in user satisfaction."),
        ],
        "qualitative": [],
        "learnings": [
            "User-centered design principles (e.g., system status visibility, error recovery) are critical for improving usability and trust.",
            "Comprehensive research (e.g., event logs, surveys, interviews) is essential for identifying pain points and designing solutions that meet user needs.",
            "Usability testing helps validate design choices and gather actionable feedback for further iteration.",
        ],
    },
    {
        "slug": "landing-pages-dorna",
        "cover_img": "https://framerusercontent.com/images/fZ1pkS8agnYCFJxMfCpxOBApYHM.jpg",
        "tag": "Ecommerce",
        "title": "Designing High-Conversion Landing Pages for Dorna Sports",
        "subtitle": "Enhancing User Engagement and Subscription Rates for MotoGP and WorldSBK",
        "role": "UI/UX design",
        "category": "Ecommerce",
        "company": "Dorna Sport",
        "website": 'https://www.motogp.com',
        "illustration": "landing",
        "intro": [
            "Between 2016 and 2021, I collaborated with Dorna Sports to design and optimize landing pages for MotoGP and WorldSBK VideoPass subscriptions.",
            "By focusing on user-centered design principles and iterative testing, we achieved significant improvements in user engagement and conversion rates.",
        ],
        "context": "Dorna Sports aimed to increase subscriptions for their MotoGP and WorldSBK VideoPass services. However, the existing landing pages lacked visual appeal and clear calls to action, resulting in suboptimal performance.",
        "problem": [
            "Low conversion rates due to unengaging landing pages.",
            "Lack of clear communication of the value of the VideoPass services.",
            "Poor user experience and navigation on the landing pages.",
        ],
        "objective": "Redesign the landing pages to improve visual appeal, user experience, and conversion rates for the VideoPass services.",
        "responsibilities": [
            "Conduct user experience analyses to identify pain points and areas for improvement.",
            "Create interactive prototypes and wireframes to visualize design solutions.",
            "Design and implement visually engaging and user-friendly landing pages.",
        ],
        "research": [
            ("UX analyses", "Conducted to identify pain points and areas for improvement."),
            ("A/B testing", "Utilized to evaluate different design approaches and determine the most effective solutions."),
        ],
        "design_blocks": [
            ("Design", "Created interactive prototypes and wireframes to visualize user flows and iterate on designs quickly, designed visually engaging layouts that effectively communicated the value of the VideoPass services, including highlighting key features (access to live and on-demand races, exclusive content, and availability in various territories), user experience optimization (intuitive navigation and clear call-to-action buttons to guide users through the subscription process), and responsive design (ensured optimal viewing experiences across all devices: desktop, tablet, mobile)."),
            ("Implementation", "Collaborated with development teams to implement the redesigned landing pages, and monitored user engagement and conversion rates post-launch to measure the impact of the changes."),
        ],
        "impact": [
            ("Increased user engagement", "The visually engaging layouts and multimedia elements captured users' attention and interest."),
            ("Higher subscription rates", "The clear calls to action and intuitive navigation led to improved conversion rates."),
            ("Enhanced user experience", "The responsive design ensured a seamless experience across all devices."),
        ],
        "qualitative": [],
        "learnings": [
            "A/B testing is a powerful tool for identifying effective design improvements.",
            "Visual appeal and clear communication of value are critical for driving conversions.",
            "Responsive design ensures a consistent and optimal experience across devices.",
        ],
    },
    {
        "slug": "roku-tv-app",
        "cover_img": "https://framerusercontent.com/images/ZRTgPOqsEFBPpnqCdGGu0cRdo.jpg",
        "tag": "TV App",
        "title": "Designing the Dorna Sports TV App for Roku",
        "subtitle": "Enhancing the Viewing Experience for MotoGP Fans",
        "role": "UI/UX design",
        "category": "TV App",
        "company": "Dorna Sport",
        "website": 'https://www.motogp.com',
        "illustration": "tv",
        "intro": [
            "I led the design of the Dorna Sports TV App for Roku, aiming to deliver an immersive and user-friendly experience for MotoGP enthusiasts.",
            "This project involved comprehensive UX research, user experience design, and UI design to meet the diverse needs of a global audience.",
        ],
        "context": "Dorna Sports aimed to expand its digital presence by offering a dedicated TV app on the Roku platform. The goal was to provide fans with seamless access to live races, on-demand content, and exclusive features.",
        "problem": [
            "Lack of a dedicated TV app for Roku users.",
            "Need for an intuitive interface that could handle live events, past races, and exclusive content.",
            "Ensuring a high-quality streaming experience for users.",
        ],
        "objective": "Design and develop a Roku TV app with an intuitive interface that provides seamless access to live races, on-demand content, and personalized features.",
        "responsibilities": [
            "Conduct UX research to understand user preferences and industry standards.",
            "Develop user personas to guide the design process.",
            "Design a clean and intuitive interface with personalized content and seamless navigation.",
            "Ensure high-quality streaming for an immersive viewing experience.",
        ],
        "research": [
            ("User interviews", "Conducted to understand fan preferences and pain points."),
            ("Competitive analysis", "Performed to identify industry standards and best practices."),
            ("User personas", "Developed to represent key user groups and guide design decisions."),
        ],
        "design_blocks": [
            ("Design", "Created a clean and intuitive interface that allowed users to easily navigate through live events, past races, and exclusive content, designed personalized content features, enabling users to customize their viewing experience by selecting favorite riders and teams and receiving tailored content recommendations, developed a user-friendly menu structure for quick access to various content categories and settings, and ensured high-quality streaming by optimizing video playback for a smooth and immersive viewing experience."),
            ("Implementation", "Collaborated with development teams to build and launch the Roku TV app, and conducted usability testing to validate the design and gather feedback for improvements."),
        ],
        "impact": [
            ("Positive user feedback", "The app received acclaim for its intuitive interface and seamless navigation."),
            ("Enhanced digital presence", "The app expanded Dorna Sports' digital offerings, providing fans with a dedicated platform to engage with MotoGP content."),
            ("Improved user engagement", "Personalized content and high-quality streaming increased user satisfaction and engagement."),
        ],
        "qualitative": [],
        "learnings": [
            "UX research is essential for understanding user preferences and guiding design decisions.",
            "Personalization enhances user engagement by tailoring the experience to individual preferences.",
            "High-quality streaming is critical for delivering an immersive and enjoyable viewing experience.",
        ],
    },
    {
        "slug": "email-marketing-dorna",
        "cover_img": "https://framerusercontent.com/images/d4nXOdOgdBcjb1Dp11Nynt8zWwU.png",
        "tag": "Marketing and Social",
        "title": "Optimizing Email Marketing Campaigns for Dorna Sports",
        "subtitle": "User Engagement and Conversion Rates through Strategic Design",
        "role": "UI/UX design",
        "category": "Marketing and Social",
        "company": "MotoGP (Dorna Sports)",
        "website": 'https://www.motogp.com',
        "illustration": "email",
        "intro": [
            "I led the design and optimization of email marketing campaigns for Dorna Sports, focusing on MotoGP and WorldSBK audiences.",
            "By implementing user-centered design principles and conducting A/B testing, we achieved significant improvements in user engagement and conversion rates.",
        ],
        "context": "Dorna Sports aimed to increase user engagement and conversion rates through their email marketing campaigns. However, the existing emails lacked visual appeal and clear calls to action, resulting in suboptimal performance.",
        "problem": [
            "Low engagement and conversion rates due to unappealing email designs.",
            "Lack of clear calls to action and effective communication of content value.",
            "Poor readability and usability of the email campaigns.",
        ],
        "objective": "Redesign the email marketing campaigns to improve visual appeal, readability, and user engagement, ultimately increasing conversion rates.",
        "responsibilities": [
            "Conduct comprehensive analyses of the user experience with email campaigns.",
            "Design visually engaging and functional email templates.",
            "Optimize email content and structure to enhance readability and usability.",
        ],
        "research": [
            ("User experience analyses", "Conducted to identify pain points and areas for improvement in the existing email campaigns."),
            ("Engagement and conversion data", "Collected and analyzed data on user engagement and conversion rates to inform design decisions."),
        ],
        "design_blocks": [
            ("Design", "Created interactive prototypes and email templates to serve as the foundation for visually appealing and functional email campaigns, designed visually engaging layouts that effectively communicated the value of the content, including clear calls to action to guide users toward desired actions and improved readability and usability through optimized content structure and design, and implemented A/B testing to evaluate different design approaches and determine the most effective solutions."),
            ("Implementation", "Collaborated with the marketing team to implement the redesigned email campaigns, and monitored user engagement and conversion rates post-launch to measure the impact of the changes."),
        ],
        "impact": [
            ("Increased user engagement", "The visually appealing layouts and clear calls to action captured users' attention and encouraged interaction."),
            ("Higher conversion rates", "The optimized email content and structure led to improved conversion rates."),
            ("Enhanced user satisfaction", "The improved readability and usability of the email campaigns resulted in higher user satisfaction."),
        ],
        "qualitative": [],
        "learnings": [
            "Visual appeal and clear calls to action are critical for driving user engagement and conversions.",
            "User experience analysis is essential for identifying pain points and guiding design improvements.",
            "A/B testing helps determine the most effective design approaches.",
        ],
    },
    {
        "slug": "desigual-product-card",
        "cover_img": "https://framerusercontent.com/images/vzJyFGpXcQ9lR7XsRFRhBVqv4Zc.jpg",
        "tag": "Ecommerce",
        "title": "Redesigning Desigual's Product Card",
        "subtitle": "Optimizing Product Presentation to Boost Conversion Rates",
        "role": "UI/UX design",
        "category": "Ecommerce",
        "company": "Desigual",
        "website": 'https://www.desigual.com',
        "illustration": "product-card",
        "intro": [
            "I led the redesign of Desigual's product card on their e-commerce platform.",
            "The goal was to create a more engaging and user-friendly interface that would enhance the shopping experience and increase conversion rates.",
        ],
        "context": "Desigual's existing product card lacked visual appeal and intuitive navigation, leading to user frustration and lower sales. The design failed to effectively highlight product features and guide users toward making a purchase.",
        "problem": [
            "Poor visual appeal and usability of the product card.",
            "Lack of clear product descriptions and prominent calls to action.",
            "Low user engagement and conversion rates.",
        ],
        "objective": "Redesign the product card to improve visual appeal, usability, and user engagement, ultimately increasing conversion rates.",
        "responsibilities": [
            "Conduct user research to identify pain points and gather insights.",
            "Collaborate with cross-functional teams to develop wireframes and prototypes.",
            "Design a clean and intuitive product card that highlights product features and facilitates easy navigation.",
        ],
        "research": [
            ("User interviews and usability testing", "Conducted to identify pain points and gather insights into user behavior."),
            ("User feedback analysis", "Analyzed to understand the key areas for improvement in the existing product card."),
        ],
        "design_blocks": [
            ("Design", "Developed wireframes and prototypes in collaboration with cross-functional teams, focusing on a clean and intuitive design, designed a visually appealing product card with high-quality images to showcase products effectively, clear product descriptions to provide essential information at a glance, and prominent call-to-action buttons to guide users toward making a purchase, and implemented interactive elements, such as zoom-in capabilities and color selection options, to enhance user engagement."),
            ("Implementation", "Collaborated with development teams to implement the redesigned product card, and conducted A/B testing to validate the effectiveness of the new design."),
        ],
        "impact": [
            ("Increased user interaction", "The interactive elements and high-quality visuals captured users' attention and encouraged engagement."),
            ("23% increase in conversion rates", "The redesigned product card led to a measurable boost in conversion rates, validating the effectiveness of the redesign."),
            ("Improved user satisfaction", "The clean design and intuitive navigation enhanced the overall shopping experience."),
        ],
        "qualitative": [],
        "learnings": [
            "User research is essential for identifying pain points and guiding design improvements.",
            "Interactive elements (e.g., zoom-in, color selection) significantly enhance user engagement.",
            "A/B testing helps validate design effectiveness and optimize for better results.",
        ],
    },
    {
        "slug": "desigual-store-locator",
        "cover_img": "https://framerusercontent.com/images/YaBCZWUNg2hxXOIdxZWP6XhA2g.jpg",
        "tag": "Ecommerce",
        "title": "Designing Desigual's Store locator for improve the user accesibility",
        "subtitle": "How to integrate a new store locator into the mobile App.",
        "role": "UI/UX design",
        "category": "Ecommerce",
        "company": "Desigual",
        "website": 'https://www.desigual.com',
        "illustration": "map",
        "intro": [
            "In 2014, I spearheaded the design of Desigual's store locator feature on their website and mobile app.",
            "The objective was to provide users with an intuitive tool to find nearby stores, thereby bridging the gap between online and offline shopping experiences.",
        ],
        "context": "Users faced difficulties locating Desigual stores due to the lack of an efficient digital tool. This led to frustration and missed opportunities for both customers and the brand.",
        "problem": [
            "No user-friendly tool to help customers find nearby Desigual stores.",
            "Lack of detailed store information (e.g., hours, available collections).",
            "Missed opportunities to drive foot traffic to physical stores.",
        ],
        "objective": "Design and develop a user-friendly store locator tool that integrates geolocation services and provides detailed store information to improve customer experience and increase foot traffic.",
        "responsibilities": [
            "Analyze user behavior and gather feedback to understand customer needs.",
            "Collaborate with the development team to design and implement the tool.",
            "Ensure the tool is intuitive, functional, and provides value to users.",
        ],
        "research": [
            ("User behavior analysis", "Conducted alongside customer feedback gathering to identify pain points and understand user needs."),
            ("Key feature identification", "Identified key features required for the store locator, such as geolocation, search filters, and detailed store information."),
        ],
        "design_blocks": [
            ("Design", "Designed a user-friendly interface that integrated geolocation services to help users find the nearest stores effortlessly, developed an interactive map with search filters (e.g., by location, store type) to enhance usability, and included detailed store information, such as hours of operation, available collections, and contact details, to provide a comprehensive user experience."),
            ("Implementation", "Collaborated with the development team to build and launch the store locator tool, and conducted usability testing to ensure the tool met user needs and expectations."),
        ],
        "impact": [
            ("Improved user satisfaction", "The intuitive design and detailed store information made it easier for users to locate stores."),
            ("Increased foot traffic", "The tool successfully drove more customers to physical stores, boosting in-store sales."),
            ("Enhanced customer experience", "The integration of digital solutions improved the overall shopping experience for Desigual customers."),
        ],
        "qualitative": [],
        "learnings": [
            "Geolocation services are essential for creating user-friendly store locator tools.",
            "Detailed store information (e.g., hours, collections) adds significant value for users.",
            "Usability testing ensures that digital tools meet user needs and deliver a seamless experience.",
        ],
    },
]

CAREER = [
    ("2025 / Pres.", "BASF Digital Solutions / Senior Product Designer",
     "Senior Product Designer specialized in Design Systems, helping the organization create scalable digital experiences by connecting Product, Design and Engineering. I define and evolve design systems, build and document reusable component libraries, and create UX standards and design guidelines. Working closely with Product Owners, UX teams and developers, I transform business requirements into scalable digital experiences, drive adoption of design systems across products and teams, and continuously improve design-to-development workflows. The role combines UX design, design system strategy, stakeholder collaboration and design operations to ensure consistency across products while accelerating delivery for both designers and developers."),
    ("2023 / 2024", "Inari.io / Product Designer",
     "Led the design of ORCA, a reinsurance SaaS platform, transforming complex data into optimised and automated designs and workflows, which increased operational efficiency by 25%. Designing wireframes, prototypes and mockups for development with Figma. Created user flows and navigation with Miro. Conducted user research (interviews, card sorting and other research methods). Actively participated in Design thinking ceremonies with Stakeholders, BO's and users. Worked on creating and updating the design system for Inari, developing and designing new components using atomic design."),
    ("2021 / 2023", "Bolttech / Product Designer",
     "Focused on improving user experiences and operational efficiency, I redesigned B2B platforms for insurance and hearing aids, leading to a 15% enhancement in customer service. Collaborating with stakeholders, I helped develop a SaaS Supply Chain system that improved resource management by 45% and created B2C portals for partners like Orange, Fnac, and Backmarket. My work also included integrating automation into the CRM through a new email template management tool and conducting user research using A/B testing to guide design decisions. Additionally, I contributed to Bolttech's design system, crafting scalable components and tokens documented in Zeroheight."),
    ("2016 / 2021", "Dorna Sport / UX UI Designer",
     "I designed the MotoGP™ VideoPass player across all platforms, improving video streaming and transcription efficiency by 20%. By reviewing and redesigning the user renewal system, we increased retention rates by 17% and lead conversions by 15%. Collaborating with developers, I created the Roku TV app and contributed to the Apple TV app design, ensuring seamless navigation and usability. My work also included developing promotional websites for various cups and designing an internal SaaS for event and calendar management, incorporating user feedback for continuous improvement. Additionally, I enhanced Motogp.com with new pages like Riders and Calendar and executed acquisition campaigns, landing pages, and social media content to boost event promotion and engagement."),
    ("2013 / 2016", "Desigual / UX UI Designer",
     "I led the redesign of Desigual's Product Detail Page (PDP), using user research and flow analysis to create wireframes and designs that boosted conversion rates by 18% through personalized recommendations and dynamic content. I introduced new features for desigual.com, including a web player and HTML5 integration for desktop and mobile, and designed and adapted the new Desigual app. Working closely with country managers, I helped launch localized sites for various markets. Additionally, I designed landing pages for user acquisition and developed social media campaigns, enhancing brand visibility and engagement."),
    ("2011 / 2013", "Bershka / Digital Designer",
     "In September 2011, our team launched the first bershka.com website, marking a milestone for the brand's digital presence. I led the digital retouching team, optimizing images for the e-commerce platform and retouching global lookbooks and photo campaigns. Additionally, I created and designed digital marketing campaigns and content, contributing to the platform's worldwide success. My work also included designing and editing videos for global marketing campaigns, ensuring a cohesive and impactful digital strategy."),
    ("2006 / 2011", "TeleToledo TV / Post Production",
     "In my first year at TeleToledo, I worked as a graphic designer, creating impactful online and offline campaigns. As my expertise grew, I transitioned to motion graphics, leading post-production and graphic editing projects for television. I also managed all visual content, including bumpers, sketches, and the company's graphic production."),
]

FEEDBACK = [
    "Javi and I worked together at Inari for 5 months, collaborating on shared design-system issues. He's an experienced designer with great ideas and deep Figma expertise. His friendliness, adaptability, and positive attitude make him a pleasure to work with.",
    "Javi is a reliable, creative designer who delivers user-centered experiences that drive business goals. A proactive team player, he collaborates seamlessly with teams and takes on challenges with enthusiasm.",
    "Javi is an exceptional teammate with remarkable Figma skills and expertise in creating mockups. His coordination with front-end teams was outstanding, and his dedication and teamwork make him an invaluable asset to any team.",
]

PROCESS_STEPS = [
    ("Understand", "01", "Before starting any project, it is important to understand the problem I want to solve, the purpose of the project, and its possible impact. We should ask questions like why the project is needed, what goals it aims to achieve, and how it fits into the overall picture."),
    ("Define", "02", "Once we understand the need, we can define the project's scope and assess our resource limits. This includes identifying the minimum viable product (MVP) — the essential version designed to satisfy early customers and gather feedback for future improvements."),
    ("Research", "03", "Conducting research, interviews, and brainstorming sessions are essential steps to gather insights, ideas, and feedback from various stakeholders, including end-users and the development team."),
    ("Design & Prototype", "04", "Based on the insights gathered, we can start creating quick designs and prototypes to visualize potential solutions. These designs help to refine ideas, validate assumptions, and communicate the proposed solution effectively."),
    ("Test", "05", "Once we have a solid proposal and initial designs, it's important to test them with end-users to gather feedback and identify any usability issues or areas for improvement."),
    ("Results", "06", "After gathering feedback and testing the MVP, the next step is to iterate on the design and development based on the insights gained, adding new features, and measuring results against predefined metrics."),
]
