# -*- coding: utf-8 -*-
"""Content data for all 10 case studies, the projects grid, and shared copy.

Images and external links are hotlinked from the real, currently-live
javidesignlabs.com (Framer) CDN — these are Javi's own published assets.
"""

PROFILE = {
    # Change BASE_URL to "https://javidesignlabs.com" when you point your custom domain here
    "base_url": "https://javidesignlabs.github.io/myporfolio",
    # Microsoft Clarity: paste your project ID from clarity.microsoft.com (Settings → Overview).
    # Leave empty ("") to disable analytics entirely (no banner will be shown).
    "clarity_id": "xja19yd80b",
    "avatar_hero": "https://framerusercontent.com/images/Bv3kCGt7CVS9r8dtdbxDJa5hHY.jpeg",
    "avatar_about": "https://framerusercontent.com/images/UdHGJxJMIvCQPbsnF3793NhTyzw.jpg",
    "avatar_footer": "https://framerusercontent.com/images/P6TXEOXYaHG6z5IeGjc5TZIwFXM.jpg",
    "hero_graphic": "https://framerusercontent.com/images/EMwh8pAhkhVzPNPRsoohSuFfQ.jpeg",
    "linkedin": "https://www.linkedin.com/in/jdelacruztel/?locale=en_US",
    "x": "https://x.com/bynneh",
    "cal": "https://cal.com/jdlct81",
    "resume": "https://www.dropbox.com/scl/fi/cnsw0qy0hy00ilttjgrl9/Resume_2025.pdf?rlkey=vtqt9nx7dcgjkg0xly9ipgd5j&st=5209p04e&dl=0",
    "mailto": "hello@javidesignlabs.com",
    "email_display": "hello@javidesignlabs.com",
}

NAV = [
    ("Projects", "projects.html"),
    ("About & Contact", "about.html"),
]

CLIENTS = ["MotoGP", "Bolttech", "BASF", "Desigual", "Inari.io", "Bershka", "WorldSBK", "Gluecharm"]

# Real, sourced metrics pulled from the case studies / career history.
# Each figure must match its case study exactly — the "how it was measured"
# line is what makes "measured, not claimed" true.
PROOF = [
    ("40", "%", "more operational efficiency in the Bolttech supply-chain SaaS",
     "Bolttech · 2022–23", "Measured against the manual Excel process it replaced.",
     "saas-supply-chain"),
    ("23", "%", "conversion lift after redesigning Desigual's product card",
     "Desigual · 2013–16", "A/B tested against the previous product card.",
     "desigual-product-card"),
    ("17", "%", "retention increase on MotoGP VideoPass renewals",
     "Dorna Sports · 2019", "Renewal rate before vs. after the redesign.",
     "payment-renewal"),
    ("15", "%", "faster access times across Bolttech partner portals",
     "Bolttech · 2021–23", "Time-to-task from portal analytics, pre/post launch.",
     "partner-portals"),
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
        "slug": "basf-design-system",
        "cover_img": "assets/img/basf-design-system/cover.svg",
        "tag": "Design system",
        "title": "Consolidating Legacy Design Systems into One Token-Based Library",
        "subtitle": "Connecting Product, Design and Engineering across a global agricultural platform",
        "role": "Senior Product Designer — I own the design system",
        "authorship": "I define the token architecture, build and document the library, and run the component QA. The products themselves are designed by teams across regions — my job is the system they all build on, and reviewing what ships against it.",
        "category": "Design system · Enterprise",
        "company": "BASF Digital Solutions",
        "website": None,
        "illustration": "design-system",
        "outcome": "One token-based library replacing several legacy systems",
        "nda": "Described at a structural level: diagrams are my own redrawings and no production interface, client data or internal tooling appears. Happy to walk through the real work in a call.",
        "intro": [
            "I lead the design system work at BASF Digital Solutions, consolidating several legacy systems into a single token-based library behind a global customer portal — catalogue, orders, financial documents, service and account, in multiple countries and languages.",
            "The job is less about drawing components and more about making one set of decisions hold across teams, markets and codebases — and keeping design and engineering pointed at the same source.",
        ],
        "context": "The portal is one product on paper and a dozen in practice: a catalogue and product pages, a cart and checkout, order visibility, financial documents, a service area and account settings — each with per-market variants, its own language handling and its own consent rules. Those areas had grown their own design languages over the years: their own buttons, their own spacing logic, their own idea of what \"error red\" meant. Teams in different regions shipped interfaces recognisable as the same company only by the logo, and every new feature began by rebuilding something that already existed elsewhere.",
        "problem": [
            "Several parallel design systems, none of them complete, all of them diverging.",
            "Every pattern has to survive translation, a different market's rules and a different content length — so a component that only works in one language is not finished.",
            "No shared vocabulary between designers and developers — handoff was a conversation, repeated per feature.",
            "Documentation lived in tools engineers did not open, so it was always slightly out of date.",
            "No way to know what was actually in production versus what the library said should be.",
        ],
        "objective": "Build one token-based design system that teams adopt because it is faster than not adopting it — and keep it honest by generating its documentation from the design files themselves.",
        "responsibilities": [
            "Define the token architecture and the naming that holds it together.",
            "Build and document the component library, with accessibility specified rather than assumed.",
            "Run the inventory and QA that tells us what is really shipping.",
            "Work with product owners and developers to turn requirements into components the system already has.",
        ],
        "research": [
            ("Component inventory of the live product", "Rather than guess at the gap between library and reality, I wrote a crawler that walks the live site, screenshots every component it finds and files one markdown page per component. It produced 40 component pages — and a clear list of what had drifted, what was duplicated, and what had been built one-off."),
            ("Working sessions with engineering", "I sat with the developers consuming the library to find where the handoff actually broke. The answer was rarely the visual spec; it was missing states, undefined edge cases and props that did not map to anything in Figma."),
            ("Density feedback from real users", "Users told us the interface felt oversized on dense data screens. That fed a layout-density initiative — prototyped in HTML so stakeholders could feel the difference rather than judge it from a static frame."),
        ],
        "design_blocks": [
            ("Three-tier tokens — the decision that paid for itself at the first rebrand", "Tokens are split into primitives (the raw palette and scale), semantic names that carry meaning rather than appearance — text, surface, stroke, icon and form roles — and component-level bindings on top. Components never reference a raw value. It is more structure up front, and it stopped being theoretical the first time a brand refresh had to roll across the whole portal: that became a remapping job instead of a hunt through component files."),
            ("Spacing scoped by where it applies", "The spacing scale is not one global ramp. It is split by context — space inside a component, space between blocks, space across a page — so a designer choosing spacing is choosing the <i>kind</i> of gap, not guessing a number. It is the single change that most reduced the \"why is this 12 and that 16\" conversation in reviews."),
            ("One interaction pattern instead of four", "Several areas of the portal needed the same move: open a detail layer over a list without losing your place. The tempting route was to solve it locally in each area. I explored it once as a shared pattern and tested it against all of them, because four bespoke solutions would have been four things to maintain and four things for a user to learn."),
            ("Documentation generated, not written", "Handoff specs are generated from the design file and published to the engineering wiki, beside the tickets. Writing them by hand guarantees drift: the doc is accurate the day you write it and wrong a month later. I documented 14 components this way, each with the same five sections — anatomy, states, props, tokens, accessibility — so the shape is learned once and skimmed thereafter."),
            ("Decisions recorded next to the work", "Each area of the portal carries its own notes alongside the designs: what was decided, what was rejected and why. Six months later the question is never \"what does this look like\" — it is \"why is it like this\", and that answer is the one that normally walks out of the door with whoever made it."),
            ("Adoption treated as a design problem", "A system nobody uses is a hobby. I ran the component QA myself — checking the built Angular components against the Figma source for visual fidelity, behaviour, accessibility and API — and fixed token bindings where they had come loose. Reviewing the implementation is what keeps the library trustworthy enough to be worth adopting."),
        ],
        "impact": [
            ("One library across the whole portal", "A single token-based system now backs the catalogue, ordering, financial, service and account areas, replacing the parallel legacy systems."),
            ("40 components inventoried, 14 fully documented", "The inventory is automated, so the gap between library and production is a report rather than an argument."),
            ("Faster, quieter handoff", "Specs arrive with the ticket instead of being negotiated per feature — the recurring design-to-dev conversation largely disappeared."),
            ("A brand refresh became a remap", "Rolling a visual refresh across the system meant changing the semantic layer, not reopening every component."),
        ],
        "qualitative": [
            "Designers reach for the system first, because it is now the shortest path rather than the correct-but-slower one.",
            "Engineering and design argue about the same artifact instead of about two different ones.",
        ],
        "gallery_dir": "basf-design-system",
        "gallery_ext": "svg",
        "gallery": [
            ("tokens", "Three-tier token architecture — components bind to semantic names, never to raw values. Redrawn generically."),
            ("handoff", "Every handoff page has the same five sections, generated from the Figma file and published where engineers already work."),
            ("inventory", "The automated inventory: crawl the live product, compare against the library, publish one page per component."),
        ],
        "learnings": [
            "A semantic layer feels like over-engineering right up until the first brand change — then it is the only reason the work is survivable.",
            "Multi-market is a design-system problem before it is a translation problem. A component that assumes one language\'s word length, one market\'s consent rules or one country\'s checkout has to be rebuilt on contact with the second market.",
            "Documentation that is written by hand will drift; documentation that is generated stays true.",
            "Adoption is not a rollout email. It comes from reviewing implementations and making the system the fastest route.",
        ],
    },
    {
        "slug": "familyhub",
        "outcome": "One design system across PWA, iOS and Android",
        "cover_img": "assets/img/familyhub/cover.webp",
        "gallery": [
            ("home", "Home — today's menu for the baby and the family, plus pending tasks and voice input."),
            ("cocina", "Kitchen hub — baby recipes, batch cooking, the weekly planner and the shopping list."),
            ("recetas", "Baby-led weaning recipes filtered by age range and meal, with favourites."),
            ("batch", "Batch cooking — a weekly menu generated with AI in one tap."),
            ("lista", "Shopping list grouped by who it's for, with progress tracking."),
            ("tareas", "Shared tasks with owners, urgency, filters and a live activity banner."),
            ("nueva", "New task — a bottom sheet with assignee and urgency in three taps."),
            ("perfil", "Profile — personal stats and push notifications for partner updates."),
        ],
        "tag": "PWA & Native apps",
        "title": "FamilyHub: Designing and Building a Self-Hosted Family Platform",
        "subtitle": "From a single recipe tool to a PWA and native iOS/Android apps — designed, built and hosted end to end",
        "role": "Everything — design, build and infrastructure",
        "authorship": "A personal project, so this one is entirely mine: product decisions, design system, PWA, native iOS and Android apps, backend and the server it runs on.",
        "category": "PWA · iOS · Android",
        "company": "Personal project",
        "website": None,
        "illustration": "product-card",
        "intro": [
            "FamilyHub is a family management platform I designed and built end to end: a progressive web app plus native iOS and Android apps, all running on a Synology NAS at home.",
            "It started as a small recipe tool and grew, module by module, into the place where our family's day-to-day information lives.",
        ],
        "context": "Family logistics tend to be scattered: recipes in one app, doctors' phone numbers in another, shared expenses in a spreadsheet, reminders in a group chat. FamilyHub began as a baby-led weaning (BLW) recipe tool and kept expanding as the same fragmentation showed up in other parts of family life.",
        "problem": [
            "Family information spread across chats, notes and disconnected apps.",
            "No single place for shared tasks, expenses and key contacts such as medical providers.",
            "Off-the-shelf tools meant handing personal family data to third-party services.",
        ],
        "objective": "Design and build one coherent platform for family life — consistent across web, iOS and Android — with all data self-hosted on our own hardware.",
        "responsibilities": [
            "Product definition and scoping each new module.",
            "Design system and UI design across three platforms.",
            "Full-stack development: PWA, backend, native iOS and Android apps.",
            "Self-hosted infrastructure and deployment on a home NAS.",
        ],
        "research": [
            ("Origin", "The first version solved one concrete need: planning baby-led weaning recipes. Using it daily made it obvious which other family workflows needed the same treatment."),
            ("Scope evolution", "Rather than planning a big platform upfront, FamilyHub grew one module at a time — contacts and medical providers, tasks, shared expenses, and push notifications — each added when a real need appeared."),
        ],
        "design_blocks": [
            ("Design system", "A warm terracotta, cream and sage palette with Nunito as the typeface, designed to feel calm and domestic rather than corporate. The system was sourced from a Figma Make file and brought into code through Figma MCP, keeping design and implementation in sync."),
            ("Modules", "A kitchen hub with baby-led weaning recipes filtered by age, AI-generated batch-cooking menus, a weekly planner and a shopping list; shared tasks with owners, urgency and voice input; plus contacts and medical providers, shared expenses and push notifications. Every module is built on the same components and patterns, so the platform feels like one product, not a collection of tools."),
            ("Native apps", "Beyond the PWA, I built native apps for iOS in SwiftUI and for Android in Kotlin with Jetpack Compose, translating the same design system to each platform's conventions."),
            ("Infrastructure", "The backend is PocketBase running in Docker on a Synology DS925+ NAS. Push notifications are delivered through Firebase Cloud Messaging from a separate Docker container."),
            ("Where AI did the work, and where I did", "I used Figma Make to get the first visual direction out quickly, and Figma MCP to pull the design system straight into code instead of re-typing values by hand. That is genuinely faster — but it is also where the thinking stops and the judgement has to start. <b>The tools produced:</b> first-pass layouts, a palette to react to, and the token-to-code plumbing. <b>I decided:</b> that it should feel domestic rather than corporate, which modules existed at all and in what order, what belonged on the home screen versus a tab, and the whole information architecture. <b>How I checked it:</b> by using it daily with my family. Several AI-suggested layouts looked fine in Figma and were wrong in the kitchen with one hand full — those got rebuilt. The honest summary is that AI compressed the production time and changed none of the product decisions."),
        ],
        "impact": [
            ("One system, three platforms", "A single design system shared across the PWA, SwiftUI and Jetpack Compose apps."),
            ("Fully self-hosted", "Family data stays on our own hardware, with no dependency on third-party SaaS for storage."),
            ("End-to-end ownership", "From Figma to Docker: product, design, frontend, native apps, backend and infrastructure by one person."),
        ],
        "qualitative": [],
        "learnings": [
            "Growing a product one real need at a time keeps scope honest.",
            "A shared design system is what makes a multi-platform product feel like one product.",
            "Building across the full stack sharpens design decisions — you feel every constraint firsthand.",
        ],
    },
    {
        "slug": "saas-supply-chain",
        "outcome": "40% more operational efficiency",
        "cover_img": "https://framerusercontent.com/images/BpCaafId9OJ1JASCegLAJX3k.jpg",
        "tag": "SaaS",
        "title": "SaaS Supply Chain Service",
        "subtitle": "Optimizing Repair Center Management: A User-Centered Approach to Streamline Operations and Enhance Customer Experience",
        "role": "Lead designer — sole designer on the product",
        "authorship": "I was the only designer on this: research with all three teams, the roadmap to MVP, and every screen. Engineering built it; the supply-chain team owned the business rules I designed around.",
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
            ("40% increase in operational efficiency", "Measured against the manual Excel-and-email process it replaced: hours spent per weekly update, before vs. after."),
            ("Repair-centre lookups moved into the platform", "Customer Service stopped keeping a second window open on an external spreadsheet to answer a routine question."),
            ("Scalable and modular system", "Ready for continuous improvements and optimized loading times."),
        ],
        "qualitative": [
            "Greater autonomy for Repair Centers, while maintaining full connectivity with the Supply Chain team.",
            "Improved collaboration between teams, eliminating communication inconsistencies.",
        ],
        "learnings": [
            "Three teams described the same breakdown in three different ways — and none of them had the whole picture. Supply Chain saw a tedious spreadsheet, Customer Service saw slow lookups, the repair centres saw nobody reading their updates. It was one problem wearing three costumes.",
            "Shadowing beat interviewing here. Customer Service told me the search was \"a bit slow\"; watching them do it showed they had a second window open permanently, because the real tool had never been integrated.",
            "I let the repair centres keep a file-based workflow instead of pushing them into a portal. A weekly JSON upload fit how they already worked — and a design they would actually use beat the tidier one I had sketched first.",
        ],
    },
    {
        "slug": "bolttech-design-system",
        "outcome": "Components and tokens for the first shared library",
        "cover_img": "https://framerusercontent.com/images/frKhVknw8YUYEnhirTjNLuXz3e4.png",
        "tag": "Design system",
        "title": "Contributing to Bolttech's Design System: Components and Tokens",
        "subtitle": "Building the pieces of a shared library for an insurtech scaling across markets",
        "role": "Product Designer — contributor to the design system",
        "authorship": "I was one of several designers on this. The system itself was led by the design team as a whole; my part was designing components and their states, creating the design tokens in Figma, and documenting what I built in Zeroheight. The brand guidelines came from marketing, and the front-end implementation was the developers'. The decisions below are the ones I argued for in my corner of it, not the system's strategy.",
        "category": "Design system",
        "company": "Bolttech",
        "website": 'https://bolttech.io/distribution-engine/',
        "illustration": "design-system",
        "intro": [
            "Bolttech was shipping insurance products across several markets with no shared component library. The design team built the first one, and I worked on its components, tokens and documentation.",
            "It was my first time building inside a system rather than designing screens — and the first time I had to think about a component as something other people would use in situations I would never see.",
        ],
        "context": "The company was growing fast, with separate teams building B2B partner portals and B2C customer journeys. Each had accumulated its own buttons, form fields and modals. Nothing was shared, so every new screen started by copying the nearest existing one and editing it — which meant every inconsistency propagated and compounded.",
        "problem": [
            "Components re-invented per team, with no agreement on states, spacing or interaction.",
            "Designers and developers describing the same element in two different vocabularies.",
            "No single place to check what the correct version of anything was.",
        ],
        "objective": "Give the team a shared library with tokens that worked the same way in Figma and in code, so handoff stopped being a translation exercise.",
        "responsibilities": [
            "Design components and every one of their states.",
            "Create the design tokens in Figma.",
            "Document the components I built in Zeroheight.",
            "Review implementations with the developers consuming them.",
        ],
        "research": [
            ("Audit of what already existed", "Before designing anything I collected every button, input and modal in use across the products. Seeing them side by side made the case better than any argument could have: there were nine button styles doing the same job."),
            ("Conversations with the developers", "I asked what actually slowed them down. It was not the visuals — it was the missing states. A spec with only the default state meant inventing hover, disabled and loading themselves, differently each time."),
        ],
        "design_blocks": [
            ("The argument I made: tokens, not a style guide", "The quick option was a style guide listing hex values. I pushed for named tokens used identically in Figma and in the CSS, because a style guide describes decisions while a token enforces them — change one and both sides update. It is the thing that stopped design and engineering describing the same colour in two vocabularies."),
            ("What I insisted on: every variant ships with all five states", "For the components I owned, each one specified default, hover, focus, loading and disabled — not just the happy path. It roughly triples the work up front, and it is where the consistency actually came from, because the inconsistency was never in the default state. It also made the focus ring non-negotiable instead of something added later, if at all."),
            ("What I learned from the documentation", "I documented my components in Zeroheight — usage, props and accessibility, the things a Figma file cannot tell a developer. Writing them taught me how much of a component's behaviour I had been holding in my head and never writing down."),
            ("Reviewing the build", "I checked early implementations of my components against the library. A component that is published but never reviewed quietly becomes a suggestion."),
        ],
        "impact": [
            ("Nine button styles collapsed into one set", "The audit's inconsistencies became a single set of components shared by the B2B and B2C products."),
            ("Handoff stopped being a conversation", "With tokens named identically on both sides and every state specified, the recurring per-feature spec discussion largely went away for the components we had covered."),
            ("A foundation the team kept building on", "The system outlived my time there, which is the only durable test of whether one worked."),
        ],
        "qualitative": [
            "Designers stopped copying old screens as a starting point, because pulling from the library was faster.",
            "Reviews moved from \"is this the right blue\" to questions actually worth a designer's time.",
        ],
        "learnings": [
            "The audit was the most persuasive artifact in the project. Nine buttons in a row made the case instantly; a written argument would not have.",
            "Specifying all states is unglamorous and is where the consistency actually comes from.",
            "Contributing to someone else's system taught me more about adoption than leading one would have: you feel every bit of friction you would otherwise have designed away for yourself.",
        ],
        "gallery_dir": "bolttech-design-system",
        "gallery_ext": "svg",
        "gallery": [
            ("components", "The components I owned, specified in all five states — where the consistency actually came from."),
            ("tokens", "Tokens named identically in Figma and in code, so handoff stopped being a translation step."),
            ("docs", "Documentation in Zeroheight: usage, props and accessibility — what a Figma file can't tell a developer."),
        ],
    },
    {
        "slug": "partner-portals",
        "outcome": "15% faster access times",
        "cover_img": "https://framerusercontent.com/images/wvmDSEbjdRvEPLWhtyWIUhJrjnM.jpg",
        "tag": "Desktop and Mobile",
        "title": "Enhancing Partner Portals: A User-Centered Redesign for Bolttech",
        "subtitle": "Optimizing B2B and B2C Interfaces to Improve User Experience and Operational Efficiency",
        "role": "Lead designer — redesign across B2B and B2C portals",
        "authorship": "I ran the research and designed the redesigned portals. The existing codebase and its constraints were investigated together with the development team, and rollout was theirs.",
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
            "Partners like Fnac and Orange ran daily service work through portals that had grown feature by feature, with no one owning the flow across them.",
            "Access times were long enough to slow routine work — the cost was paid every single day, by people who had no alternative.",
            "Completing one task meant crossing steps that had each been designed on their own and never together.",
            "What could realistically change was bounded by the existing codebase, so the redesign had to start from what it could actually support.",
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
            ("15% improvement in access times", "Time-to-task from portal analytics, compared pre- and post-launch across Fnac and Orange portals."),
            ("Streamlined user task performance", "Reducing the time and effort required to complete tasks."),
            ("Enhanced user experience", "Leading to higher satisfaction among partners."),
        ],
        "qualitative": [
            "Increased operational efficiency for Bolttech's partners, contributing to better overall performance.",
        ],
        "gallery_dir": "partner-portals",
        "gallery_ext": "svg",
        "gallery": [
            ("constraints", "Mapping what the codebase allowed before designing is why this shipped in sprints instead of becoming a rewrite."),
        ],
        "learnings": [
            "Investigating the codebase with the developers before designing is why this shipped in sprints instead of becoming a rewrite nobody would have funded.",
            "The stakeholder reviews were slow and they are the reason the design survived contact with the business goals.",
            "Access time is what convinced people. \"More usable\" is arguable in a meeting; 15% faster ends the meeting.",
        ],
    },
    {
        "slug": "saas-process-modeling",
        "outcome": "Technical specs written by non-technical users",
        "cover_img": "https://framerusercontent.com/images/LdMym2jStT80OZnoQwnKx2fViQ.png",
        "tag": "SaaS",
        "title": "SaaS Process Modeling: Transforming ideas into technical specifications",
        "subtitle": "Leveraging AI to bridge the gap between concept and implementation",
        "role": "Product designer — co-founder of a side project",
        "authorship": "A two-person side project. I owned product definition, research and the entire interface; my co-founder built the AI pipeline behind it.",
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
            "Reducing the whole thing to three questions — what problem, how would you solve it, who is it for — was the design decision that mattered. Every extra field we considered adding made the blank page harder to start.",
            "The non-technical users were the real test. A technical analyst can work around a bad tool; a product owner just stops using it and writes the doc in a text file instead.",
            "AI was good at structure and terrible at judgement. It produced a consistent skeleton in seconds and plausible nonsense in the details, so the interface had to make editing the output as easy as generating it.",
        ],
    },
    {
        "slug": "payment-renewal",
        "outcome": "17% more renewal retention",
        "cover_img": "https://framerusercontent.com/images/cD4x3P1lTyys2SAT5dwR7XDFHc.jpg",
        "tag": "UX UI",
        "title": "Redesigning Payment and Renewal Experiences",
        "subtitle": "Optimizing User Journeys for Better Conversion Rates and Customer Satisfaction",
        "role": "Lead designer — payment and renewal flows",
        "authorship": "Mine: the event-log analysis, the interviews, the personas, and the redesigned flows and prototypes. The surveys were run with the customer service team, who also owned the post-launch monitoring.",
        "category": "UX UI",
        "company": "Dorna Sports",
        "website": None,
        "illustration": "payment",
        "intro": [
            "In 2019, the payment and product renewal processes faced significant challenges, leading to user frustration and decreased retention rates.",
            "By conducting in-depth research and leveraging user insights, I designed and implemented solutions that streamlined workflows, improved usability, and enhanced the overall user experience.",
        ],
        "context": "In 2019, users were experiencing confusion and dissatisfaction with the payment and automatic product renewal processes. This led to a poor user experience and potentially impacted customer retention and conversion rates.",
        "problem": [
            "Payment and automatic renewal were experienced as one confusing thing — users could not tell which of the two they were agreeing to.",
            "The flow reported nothing back: after submitting, nothing on screen said where you were or whether it had worked.",
            "A failed or mistaken payment had no fix in place. The only route was to start again, and the event logs show that is where people left.",
            "The satisfaction surveys and the event logs pointed at the same two moments, from opposite directions.",
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
            ("17% increase in renewal retention", "Renewal rate compared before and after the redesign. The clearer status and recovery options kept subscribers who would previously have dropped out mid-flow."),
            ("15% more lead conversions", "Measured on the same funnel over the following season."),
            ("Higher satisfaction after launch", "Usability testing before release and customer feedback after it both reported the flow as clearer — qualitative, not a number."),
        ],
        "qualitative": [],
        "gallery_dir": "payment-renewal",
        "gallery_ext": "svg",
        "gallery": [
            ("flow", "The two points the event logs and the surveys both pointed at — and the two changes that answered them."),
        ],
        "learnings": [
            "System status and error recovery read like textbook heuristics until you open an event log and find the drop-offs sitting exactly where the interface stopped telling people anything.",
            "The surveys said people were unhappy; the logs said where. Either one on its own would have sent me to the wrong screen.",
            "Renewals are not a checkout problem. People abandon them for a different reason — not knowing what they already agreed to.",
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
        "company": "Dorna Sports",
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
        "outcome": "VideoPass brought to living-room TV",
        "cover_img": "https://framerusercontent.com/images/ZRTgPOqsEFBPpnqCdGGu0cRdo.jpg",
        "tag": "TV App",
        "title": "Designing the Dorna Sports TV App for Roku",
        "subtitle": "Enhancing the Viewing Experience for MotoGP Fans",
        "role": "Lead designer — TV app for Roku",
        "authorship": "I owned the UX research, personas and the full interface for the TV platform. The Roku build was done by the development team; I reviewed it against the designs.",
        "category": "TV App",
        "company": "Dorna Sports",
        "website": 'https://www.motogp.com',
        "illustration": "tv",
        "intro": [
            "I led the design of the Dorna Sports TV App for Roku, aiming to deliver an immersive and user-friendly experience for MotoGP enthusiasts.",
            "This project involved comprehensive UX research, user experience design, and UI design to meet the diverse needs of a global audience.",
        ],
        "context": "Dorna Sports aimed to expand its digital presence by offering a dedicated TV app on the Roku platform. The goal was to provide fans with seamless access to live races, on-demand content, and exclusive features.",
        "problem": [
            "MotoGP fans on Roku had no app at all — the only route to a race was a browser on another device.",
            "Three kinds of content had to share one home: a race happening right now, an archive going back years, and extras. They compete for the same space and only one of them is urgent.",
            "A TV is driven with five buttons from across a room. Patterns that work with a cursor — hover, dense menus, small targets — are unusable there.",
            "A global audience meant someone always lands mid-season, mid-weekend, in the wrong timezone.",
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
            ("No funnel data on this one", "Unlike the renewal work, I never got access to the platform analytics — so what follows is qualitative, and I\'d rather say that than dress it up."),
            ("Positive user feedback", "The app was received well for its navigation and how quickly you could get to a race — reported through the support channel, not measured."),
            ("Enhanced digital presence", "The app expanded Dorna Sports' digital offerings, providing fans with a dedicated platform to engage with MotoGP content."),
            ("A shorter path to the race", "Favourite riders and teams turned the common case — \"is my rider on?\" — into one click from the home screen."),
        ],
        "qualitative": [],
        "learnings": [
            "Designing for a remote control strips a design back to essentials. With five buttons and no pointer, every extra level of navigation is felt immediately — it taught me more about hierarchy than any desktop project had.",
            "\"What is on now\" has to win the screen. The archive is bigger and more impressive, and almost nobody opens the app for it.",
            "Letting fans pick riders and teams was less about personalisation as a feature and more about shortening the path: a favourite turns a browse into a single click.",
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
        "company": "Dorna Sports",
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
        "outcome": "23% conversion lift, A/B tested",
        "cover_img": "https://framerusercontent.com/images/vzJyFGpXcQ9lR7XsRFRhBVqv4Zc.jpg",
        "tag": "Ecommerce",
        "title": "Redesigning Desigual's Product Card on the PDP",
        "subtitle": "Optimizing Product Presentation to Boost Conversion Rates",
        "role": "Lead designer — product card redesign",
        "authorship": "I led the research, wireframes and final design of the card. The A/B test was set up with the e-commerce analytics team, and front-end development was in-house.",
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
            "The card showed the garment small and flat — on a brand whose entire proposition is pattern and colour.",
            "There was no way to inspect anything: no zoom, no switching colourway without leaving the card.",
            "The essentials were not available at a glance, so shoppers had to dig to find out what the product actually was.",
            "The call to action did not stand out, which left the path from interest to basket unclear.",
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
            ("23% increase in conversion rates", "A/B tested against the previous product card on live traffic — the redesign was rolled out only after it won."),
            ("Improved user satisfaction", "The clean design and intuitive navigation enhanced the overall shopping experience."),
        ],
        "qualitative": [],
        "gallery_dir": "desigual-product-card",
        "gallery_ext": "svg",
        "gallery": [
            ("anatomy", "What changed on the card, and why each change earned its place — validated by A/B test before rollout."),
        ],
        "learnings": [
            "On a brand built on print and colour, zoom and colour switching were not embellishments — they were the product information.",
            "The A/B test is what made the redesign defensible. Without it, 23% would have been a story about my taste.",
            "Setting the test up with the e-commerce analytics team is the only reason the number means anything.",
        ],
    },
    {
        "slug": "desigual-store-locator",
        "cover_img": "https://framerusercontent.com/images/YaBCZWUNg2hxXOIdxZWP6XhA2g.jpg",
        "tag": "Ecommerce",
        "title": "Designing Desigual's Store Locator to Improve Accessibility",
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
     "Focused on improving user experiences and operational efficiency, I redesigned B2B partner portals for insurance and hearing aids, cutting access times by 15% and streamlining the tasks service teams ran every day. Collaborating with stakeholders, I helped develop a SaaS Supply Chain system that improved operational efficiency by 40% and created B2C portals for partners like Orange, Fnac, and Backmarket. My work also included integrating automation into the CRM through a new email template management tool and conducting user research using A/B testing to guide design decisions. Additionally, I contributed to Bolttech's design system, crafting scalable components and tokens documented in Zeroheight."),
    ("2016 / 2021", "Dorna Sports / UX UI Designer",
     "I designed the MotoGP™ VideoPass player across all platforms, improving video streaming and transcription efficiency by 20%. By reviewing and redesigning the user renewal system, we increased retention rates by 17% and lead conversions by 15%. Collaborating with developers, I created the Roku TV app and contributed to the Apple TV app design, ensuring seamless navigation and usability. My work also included developing promotional websites for various cups and designing an internal SaaS for event and calendar management, incorporating user feedback for continuous improvement. Additionally, I enhanced Motogp.com with new pages like Riders and Calendar and executed acquisition campaigns, landing pages, and social media content to boost event promotion and engagement."),
    ("2013 / 2016", "Desigual / UX UI Designer",
     "I led the redesign of Desigual's product card on the Product Detail Page (PDP), using user research and flow analysis to create wireframes and designs that boosted conversion rates by 23% through personalized recommendations and dynamic content. I introduced new features for desigual.com, including a web player and HTML5 integration for desktop and mobile, and designed and adapted the new Desigual app. Working closely with country managers, I helped launch localized sites for various markets. Additionally, I designed landing pages for user acquisition and developed social media campaigns, enhancing brand visibility and engagement."),
    ("2011 / 2013", "Bershka / Digital Designer",
     "In September 2011, our team launched the first bershka.com website, marking a milestone for the brand's digital presence. I led the digital retouching team, optimizing images for the e-commerce platform and retouching global lookbooks and photo campaigns. Additionally, I created and designed digital marketing campaigns and content, contributing to the platform's worldwide success. My work also included designing and editing videos for global marketing campaigns, ensuring a cohesive and impactful digital strategy."),
    ("2006 / 2011", "TeleToledo TV / Post Production",
     "In my first year at TeleToledo, I worked as a graphic designer, creating impactful online and offline campaigns. As my expertise grew, I transitioned to motion graphics, leading post-production and graphic editing projects for television. I also managed all visual content, including bumpers, sketches, and the company's graphic production."),
]

FEEDBACK = [
    # Quoted verbatim from the original recommendations — do not paraphrase,
    # shorten, or "improve" these. They are other people's words.
    "Javier and I worked together at Inari for 9 months, collaborating on shared design system issues. He's an experienced designer with great ideas and deep Figma expertise. His friendliness, adaptability, and positive attitude make him a pleasure to work with.",
    "Javier is a reliable, creative designer who delivers user-centered experiences that drive business goals. A proactive team player, he collaborates seamlessly with teams and takes on challenges with enthusiasm.",
    "Javi is an exceptional teammate with remarkable Figma skills and expertise in creating mockups. His coordination with front-end teams is outstanding, and his dedication and teamwork make him an invaluable asset to any team.",
]

PROCESS_STEPS = [
    ("Find the real problem", "01", "The brief is rarely the problem. I start by asking who is actually stuck and what they do instead today — the workaround usually tells you more than the request did."),
    ("Draw the smallest version", "02", "I'd rather ship a narrow thing that works than a complete thing that waits. Scope is a design decision, so I make it deliberately and early."),
    ("Go and look", "03", "Interviews help, but watching someone work helps more. Most of what I've fixed came from seeing a workaround nobody had thought to mention."),
    ("Build something to react to", "04", "Prototypes beat descriptions. When the question is about density or rhythm I build it in HTML, because you can't feel a layout from a static frame."),
    ("Test before it's finished", "05", "Testing a design you're already attached to is theatre. I put it in front of people while changing it is still cheap."),
    ("Measure, then say so", "06", "A number only counts if you can say how it was measured. Everything on this site comes with its source — that's the point of the whole thing."),
]


# ---------------------------------------------------------------------------
# Portfolio curation
# ---------------------------------------------------------------------------
# Retired from the site: pre-2016 work and marketing-led pieces that don't
# support a senior design-systems profile. The case files stay in git history;
# they're simply not published or linked any more.
_RETIRED = {
    "email-marketing-dorna",    # marketing campaigns, off-target for the role
    "landing-pages-dorna",      # marketing/acquisition, overlaps payment-renewal
    "desigual-store-locator",   # 2014, too old to represent current practice
}

# Deliberate order: design-system work first, then SaaS depth, then the rest.
_ORDER = [
    "basf-design-system",       # current DS leadership — the lead card
    "bolttech-design-system",   # DS built end to end
    "saas-supply-chain",        # SaaS product depth, 40%
    "familyhub",                # end-to-end ownership, design + build
    "partner-portals",          # B2B/B2C at scale, 15%
    "payment-renewal",          # measured retention work, 17%
    "saas-process-modeling",    # AI-assisted product design
    "desigual-product-card",    # e-commerce conversion, 23%
    "roku-tv-app",              # platform breadth
]

_by_slug = {p["slug"]: p for p in PROJECTS if p["slug"] not in _RETIRED}
PROJECTS = [_by_slug[s] for s in _ORDER if s in _by_slug]

# How many cases the home page shows (UXfolio: most reviewers prefer 3–4).
HOME_FEATURED = 4
