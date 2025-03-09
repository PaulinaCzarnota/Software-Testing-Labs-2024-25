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
