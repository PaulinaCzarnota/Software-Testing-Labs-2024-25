This repository contains a collection of labs from the Software Testing module in my third year of Computer Science at TU Dublin.

# Lab Summaries

Each lab covers different testing methodologies and techniques, including unit testing, test-driven development (TDD), system testing, and business requirements validation.

### Lab 1: The Language of Software Testing

Lab 1 focuses on understanding the fundamental concepts of software testing, including errors, defects, failures, and root causes. It introduces the psychological aspects of testing and emphasizes the importance of thorough testing to prevent software failures.

#### Key Topics Covered:

- **Errors, Defects, and Failures:**  
  - **Mariner 1 Disaster**: A single missing bar in an equation caused the spacecraft to veer off-course, resulting in mission failure.  
  - **Image Upload Disaster**: Weak security controls allowed malicious scripts to be executed on a public website.
    
- **Lecture 1 Review:**  
  - Why testing is essential.  
  - Different testing objects (code, requirements, design, UI, security).  
  - Psychological factors in testing (biases, mindset of testers).
    
- **Stormboard Activity:**  
  - Collaborative exercise mapping out key testing concepts.

### Lab 2: Testing Throughout the Software Development Lifecycle

Lab 2 explores how testing integrates into the software development lifecycle (SDLC), focusing on the V-Model approach. It introduces requirements modeling, acceptance testing, and system design.

#### Key Topics Covered:

- **Business Requirements Modeling:**  
  - Extracting clear, testable requirements from vague client communication.
    
- **Acceptance Testing (UAT):**  
  - Validating the system against business requirements (e.g., verifying scanned product totals, handling payment methods, enforcing rounding rules).
    
- **System Design & Testing:**  
  - Creating a structured system architecture to support software functionality.  

#### Technologies & Tools Used:

- **YouTrack:** Bug tracking and test management.  
- **Python unittest framework:** For system testing.  
- **Test Case Development:** Defining functional and non-functional system requirements.

### Lab 3: Unit Testing and Test-Driven Development (TDD)

Lab 3 focuses on unit testing and test-driven development (TDD). It introduces writing unit tests for defect detection, business requirements validation, and implementing a game using TDD.

#### Key Topics Covered:

- **Unit Testing for Defect Detection:**  
  - Testing and fixing bugs in a Rectangle class.
    
- **Business Requirements-Based Testing:**  
  - Validating functionality in a Calculator class.
    
- **Test-Driven Development (TDD):**  
  - Implementing a Wordle game using a TDD-first approach.
    
- **Unit Test Execution Proof:**  
  - Running tests in Visual Studio Code (VS Code).

#### Technologies & Tools Used:
- **Python unittest framework:** For unit testing.  
- **VS Code & PyCharm:** Development and test execution.  
- **TDD Process:** Writing tests first, implementing functionality, then refactoring.

### Lab 4: Black Box Testing

Lab 4 focuses on Black Box Testing, a technique that evaluates system functionality without examining internal code structure. The lab covers boundary value analysis, equivalence partitioning, decision table testing, and state transition testing.

#### Key Topics Covered:

- **Train Timetables:**  
  - **Defined test partitions** for full fare and saver ticket times.  
  - **Identified boundary values** (e.g., 09:30 AM, 4:00 PM, 7:30 PM).  
  - **Derived test cases** to verify ticket classification.
    
- **Rail Cards:**  
  - **Decision table testing** for discount eligibility.
    
- **Shopping Basket System:**  
  - **State transition testing** for shopping cart interactions.  
  - **Defined invalid transitions** (e.g., removing an item from an empty cart).

#### Techniques Used:

- Equivalence Partitioning
- Boundary Value Analysis 
- Decision Table Testing
- State Transition Testing

### Lab 5: White Box Testing

Lab 5 focuses on White Box Testing techniques, with an emphasis on code coverage using PyCharm. The lab involves testing the get_grade_classification function and improving coverage to 100%.

#### Key Topics Covered:

- **Code Coverage:**  
  - Using PyCharm to measure statement and decision coverage, ensuring all code paths and logic branches are tested.

- **Improving Coverage:**  
  - Adding test cases to handle edge cases (e.g., testing exactly 40.0) and improve coverage to 100%.

- **Invalid Input Testing:**  
  - Updating the function to handle non-numeric inputs (e.g., strings), raising a ValueError, and implementing tests for invalid inputs.

- **Test Creation:**  
  - Writing unit tests for grade classifications (Fail, Pass, 2.ii, 2.i, 1) and boundary cases (e.g., 39.9, 40.0).

#### Tools Used:

- **PyCharm or Visual Studio Code:** Code coverage analysis and test execution.
- **Python unittest framework:** For unit testing.

Here's the revised Lab 6 summary with both **PyCharm or VS Code** mentioned as tools, consistent with your earlier labs:

### Lab 6: Debugging 

Lab 6 focuses on practical debugging techniques and writing detailed defect reports for common coding issues. The lab includes analyzing and fixing bugs in multiple Python programs using breakpoints, call stacks, the debug console, and navigation tools in PyCharm or Visual Studio Code (VS Code). It emphasizes the process of identifying syntax, runtime, logic, and best practice errors.

#### Key Topics Covered:

- **Debugging Tools in PyCharm or VS Code:**  
  - Setting breakpoints and using the call stack to trace function execution.  
  - Using debug navigation tools (Step Over, Step Into, Step Into My Code, Step Out, Run to Cursor).  
  - Modifying variables mid-execution via the debug console.

- **Exercise 1 – Rabbit Hole Debugging:**  
  - Explored call stack navigation, variable inspection, and code path manipulation.  
  - Compared stepping into standard library code vs. user code.

- **Exercise 2 – Grader Program:**  
  - Identified and corrected 10 defects including syntax errors (e.g., unmatched parenthesis, missing colons), runtime errors (e.g., incorrect variable usage), and logic errors (e.g., improper comparisons).

- **Exercise 3 – List Flattener:**  
  - Diagnosed and resolved logic and best practice errors.  
  - Added a missing return statement and avoided shadowing Python built-in names.

- **Additional Files:**  
  - **cheshire.py:** Utility module, correctly imported and used without requiring modification.  
  - **wonderland.py:** Fixed formatting issue in message output and confirmed proper integration with `exercise1.py`.

#### Technologies & Tools Used:

- **PyCharm or Visual Studio Code (VS Code):** Breakpoint debugging, call stack inspection, variable console, and step controls.  
- **Python unittest (implicitly tested):** Debugging outputs validated by corrected program execution.  
- **Manual Defect Reporting:** Logged defect IDs, error types, and resolutions for each issue found.

Here’s a complete Lab 7 summary for your GitHub `README.md`, matching the style of your previous lab summaries:

### Lab 7: Think Aloud Protocol

Lab 7 introduces the Think Aloud Protocol (TAP), a user testing method where participants verbalize their thoughts while completing specific tasks. This lab involved a usability test of the *Habitica* app to identify potential user experience issues in real time. Roles were divided among group members as moderator, tester, and scribe. The test consisted of three workflows, followed by SUS questionnaire scoring and personal reflections.

#### Workflows & Observations:

- **Workflow 1: Create a New Task**
  - The tester expected a large “+” icon on the home page but the "New Task" button was under a less intuitive "Tasks" tab.
  - Confusion arose due to unclear task types: "To-Dos", "Dailies", and "Habits".
  - Once in the correct section, the interface was easy to use.

- **Workflow 2: Join a Party (Social Feature)**
  - The tester accidentally dismissed the invite and struggled to relocate the "Party" feature, expecting it under “Community” or “Groups”.
  - Found terminology like "Party" misleading for a productivity app.

- **Workflow 3: Customize Avatar**
  - The tester enjoyed the process but expected avatar customization under “Profile”, not “Avatar”.
  - Almost exited without saving due to the hidden placement of the "Save" button.

#### Reflections:

- **Moderator’s Reflection:**
  - Emphasized the difficulty of staying neutral while guiding the session.
  - TAP provided immediate insight into usability issues, especially due to unintuitive terminology.

- **Scribe’s Reflection:**
  - Observed that confusion stemmed from users’ expectations based on other apps.
  - TAP helped reveal *why* users struggled, not just *where* they struggled.
  - Suggested using clearer labels and more visible buttons.

#### SUS (System Usability Scale) Score:

- The tester completed a SUS questionnaire, scoring the app **80/100**, indicating good usability despite some confusing terms and hidden features.

#### Technologies & Methods Used:

- **Think Aloud Protocol (TAP):** Real-time verbalization of thoughts while navigating the interface.  
- **System Usability Scale (SUS):** Standardized usability evaluation questionnaire.  
- **Manual Note-taking:** For capturing user quotes and issues during the test.
