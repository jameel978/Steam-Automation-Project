<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Steam_icon_logo.svg/2048px-Steam_icon_logo.svg.png" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">STEAM-AUTOMATION-PROJECT</h1>
</p>
<p align="center">
    <em>Steam API & UI Automation Project</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/jameel978/Steam-Automation-Project?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/jameel978/Steam-Automation-Project?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/jameel978/Steam-Automation-Project?style=default&color=0080ff" alt="repo-top-language">
	
<p align="center">
	<!-- default option, no dependency badges. -->
</p>

<br><!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary><br>

- [ Overview](#-overview)
- [ Features](#-features)
- [ Repository Structure](#-repository-structure)
- [ Modules](#-modules)
- [ Getting Started](#-getting-started)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Tests](#-tests)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)
</details>
<hr>

##  Overview

The Steam-Automation-Project is designed to ensure functional consistency and code quality for the Steam platform through automated API and UI testing. It features a GitHub workflow file, multiple utility scripts, and various test files for different use cases like searching and shopping cart functionality. Project settings are configured using JSON files, with different browsers supported and tests executed in parallel. Utilities include collecting and generating tokens, ensuring a well-equipped project environment. The focus is on efficient testing across the Steam website and API for maximum productivity.

---

##  Features



---

##  Repository Structure

```sh
└── Steam-Automation-Project/
    ├── .github
    │   └── workflows
    ├── Docs
    │   ├──  STD.PDF
    │   ├──  STP.PDF
    │   └──  STR.PDF  
    ├── Infra
    │   ├── Api_wrapper.py
    │   ├── Browser_wrapper.py
    │   ├── Driver_instance.py
    │   ├── Jira_wrapper.py
    │   └── __pycache__
    ├── Logic
    │   ├── Steam_API
    │   └── Website
    ├── Test_Runner.py
    ├── Tests
    │   ├── Steam_API
    │   └── Steam_website
    └── Utils
        ├── Create_Tokens.py
        ├── Get_Cookies.py
        ├── Utils.py
        ├── requirements.txt
        └── selenium-server.jar
```

---

##  Modules

<details closed><summary>.</summary>

| File                                                                                               | Summary                                                                                                                                          |
| ---                                                                                                | ---                                                                                                                                              |
| [Test_Runner.py](https://github.com/jameel978/Steam-Automation-Project/blob/master/Test_Runner.py) | Runs pytest for Steam-Automation-Projects API and UI tests concurrently or serially, captures errors as Jira issues, and saves environment info. |

</details>

<details closed><summary>Infra</summary>

| File                                                                                                             | Summary                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---                                                                                                              | ---                                                                                                                                                                                                                                                                                                                                                                                                      |
| [Browser_wrapper.py](https://github.com/jameel978/Steam-Automation-Project/blob/master/Infra/Browser_wrapper.py) | Launch web browsers for UI tests by initializing browser instances and configurations in this script. The class BrowserWrapper supports Chrome, Edge, and Firefox browsers, adjusting headless mode and screen resolution based on test type. Configs are read from a JSON file.                                                                                                                         |
| [Jira_wrapper.py](https://github.com/jameel978/Steam-Automation-Project/blob/master/Infra/Jira_wrapper.py)       | This file, located under Infra/Jira_wrapper.py, establishes a connection to a Jira instance through the provided configuration settings. It includes methods to create new issues and retrieve the Allure report URL for a specified run. Enhances testing workflow integration within project architecture.                                                                                             |
| [Driver_instance.py](https://github.com/jameel978/Steam-Automation-Project/blob/master/Infra/Driver_instance.py) | Initiate a flexible and efficient web driver instance with enhanced functionality. This class, located in `Infra/Driver_instance.py`, allows interacting with page elements on a web application through methods such as getting titles, refreshing, closing, finding, sending input, and waiting for presence. Additionally, it offers allure reporting, cookies retrieval, and custom offset movement. |
| [Api_wrapper.py](https://github.com/jameel978/Steam-Automation-Project/blob/master/Infra/Api_wrapper.py)         | The `Api_wrapper.py` infuses functionality to engage Steams APIs. It sets up requests with customizable cookies and headers, enabling efficient communication between the automation project and targeted APIs. Additionally, it supports both GET and POST methods with adjustable query parameters.                                                                                                    |

</details>

<details closed><summary>Logic.Website</summary>

| File                                                                                                                 | Summary                                                                                                                                                                                                                                                                                                                                              |
| ---                                                                                                                  | ---                                                                                                                                                                                                                                                                                                                                                  |
| [Search_Page.py](https://github.com/jameel978/Steam-Automation-Project/blob/master/Logic/Website/Search_Page.py)     | Navigate through Steams search page using this Python class. Search for games by name or id, filter results based on preferences and price range, and hide owned or wishlisted games. Interact with various elements such as buttons and sliders for efficient searching.                                                                            |
| [Website_Page.py](https://github.com/jameel978/Steam-Automation-Project/blob/master/Logic/Website/Website_Page.py)   | Navigate through a website using the provided Python class, Website_page. It initializes a web driver, loads required URLs and cookies from configuration files, and automatically logs in if valid login cookies are found. The class ensures the user is taken to the home page and prepared for further interactions.                             |
| [Cart_page.py](https://github.com/jameel978/Steam-Automation-Project/blob/master/Logic/Website/Cart_page.py)         | Navigate through the repository structure, focusing on the Logic/Website/Cart_page.py file. This file extends the Website_page class and interacts with Steam's cart page using Selenium WebDriver. It provides methods to check items' names in the cart, remove all items, and determine an empty cart status, enabling automated cart management. |
| [Wishlist_Page.py](https://github.com/jameel978/Steam-Automation-Project/blob/master/Logic/Website/Wishlist_Page.py) | This Python file extends the Website_page class to manage Steam wishlists. It defines specific xpath selectors for wishlist games and elements to remove them. Methods get wishlist games count, retrieve game names, and automate removing multiple games.                                                                                          |
| [Home_Page.py](https://github.com/jameel978/Steam-Automation-Project/blob/master/Logic/Website/Home_Page.py)         | Navigate through the Home Page of Steams website using this Python class. It features search functionality by writing text input and getting search suggestions or results. Interact with page elements and improve user experience on the homepage. (Refer to Logic/Website/Home_Page.py)                                                           |

</details>

<details closed><summary>Logic.Website.Configs</summary>

| File                                                                                                                           | Summary                                                                                                                                                                                                                                                                                                |
| ---                                                                                                                            | ---                                                                                                                                                                                                                                                                                                    |
| [Website_URLS.json](https://github.com/jameel978/Steam-Automation-Project/blob/master/Logic/Website/Configs/Website_URLS.json) | A JSON file within the Website\_Configs folder of the project's Logic/Website module. It stores and provides easy access to essential Steam store URLs, such as the cart, home, wishlist, and search pages. This simplification enhances the architecture by centralizing web navigation requirements. |

</details>

<details closed><summary>Logic.Steam_API</summary>

| File                                                                                                                               | Summary                                                                                                                                                                                                                                                                                                                                                           |
| ---                                                                                                                                | ---                                                                                                                                                                                                                                                                                                                                                               |
| [Wishlist_API.py](https://github.com/jameel978/Steam-Automation-Project/blob/master/Logic/Steam_API/Wishlist_API.py)               | Navigate through the Steam-Automation-Projects architecture, reaching the Logic/Steam_API/Wishlist_API.py. This module serves as an interface for interacting with Steam API endpoints specifically related to managing game wishlists. It initializes configuration data and provides methods to add and remove apps from user wishlists using provided app IDs. |
| [Advanced_search_API.py](https://github.com/jameel978/Steam-Automation-Project/blob/master/Logic/Steam_API/Advanced_search_API.py) | The Advanced\_search\_API.py class facilitates complex queries to the Steam API, preparing URLs with search terms and handling response parsing to extract desired app ids for further usage in this project's architecture.                                                                                                                                      |
| [Steam_token_API.py](https://github.com/jameel978/Steam-Automation-Project/blob/master/Logic/Steam_API/Steam_token_API.py)         | A Python class within the Steam_API package initializes with a provided API wrapper. It reads config data from a JSON file and uses it to call an external API for retrieving a webapi_token, raising an exception if unsuccessful.                                                                                                                               |
| [APP_Hover_API.py](https://github.com/jameel978/Steam-Automation-Project/blob/master/Logic/Steam_API/APP_Hover_API.py)             | Navigate through Steams extensive game library using this Python API, implemented in Logic/Steam_API/APP_Hover_API.py. Interact with games by retrieving hover information such as categories, genres, and review summaries via JSON responses based on given game IDs. Configured via a separate JSON file in the repository structure.                          |
| [APP_Details_API.py](https://github.com/jameel978/Steam-Automation-Project/blob/master/Logic/Steam_API/APP_Details_API.py)         | In Logic/Steam_API/APP_Details_API.py, an API class is defined to fetch detailed information about Steam apps using their IDs. It connects to the Steam API and extracts relevant data like name, price, currency, etc., simplifying access to comprehensive app details.                                                                                         |
| [Store_Search_API.py](https://github.com/jameel978/Steam-Automation-Project/blob/master/Logic/Steam_API/Store_Search_API.py)       | This file defines the `Store_Search_API` class handling queries to retrieve search results. It initializes with an API wrapper, reads configs from a JSON file, and provides methods for fetching search results and extracting app ids and names.                                                                                                                |
| [APP_Reviews_API.py](https://github.com/jameel978/Steam-Automation-Project/blob/master/Logic/Steam_API/APP_Reviews_API.py)         | Initialize and prepare API urls; fetch and filter app reviews based on specified game ID, language, and review numbers; obtain playtime of reviews for further analysis. This Python module, named `APP_Reviews_API.py`, is designed to communicate with the Steam API and retrieve relevant app reviews and their associated metrics.                            |
| [Cart_API.py](https://github.com/jameel978/Steam-Automation-Project/blob/master/Logic/Steam_API/Cart_API.py)                       | The Logic/Steam_API/Cart_API.py file initializes the Steam API interaction, providing methods like `prepair_api_url` and `add_to_cart` to add items to users' Steam carts using provided keys, package ids, and bundle ids.                                                                                                                                       |

</details>

<details closed><summary>Logic.Steam_API.API_Configs</summary>

| File                                                                                                                                               | Summary                                                                                                                                                                                                                                                                                            |
| ---                                                                                                                                                | ---                                                                                                                                                                                                                                                                                                |
| [Cart_API.json](https://github.com/jameel978/Steam-Automation-Project/blob/master/Logic/Steam_API/API_Configs/Cart_API.json)                       | Configures API endpoint for adding items to cart in the Steam-Automation-Project. Contains base URL and optional parameters like country code and language for customizing requests. Essential for interacting with the Steam API for shopping cart functionality within the project architecture. |
| [Store_Search_API.json](https://github.com/jameel978/Steam-Automation-Project/blob/master/Logic/Steam_API/API_Configs/Store_Search_API.json)       | Store.steampowered.com/api/storesearch/>. Supports country code and language customization.                                                                                                                                                                                                        |
| [Wishlist_API.json](https://github.com/jameel978/Steam-Automation-Project/blob/master/Logic/Steam_API/API_Configs/Wishlist_API.json)               | Manages URLs for adding and removing items from Steams wishlist within the project's Steam API module."                                                                                                                                                                                            |
| [APP_Reviews_API.json](https://github.com/jameel978/Steam-Automation-Project/blob/master/Logic/Steam_API/API_Configs/APP_Reviews_API.json)         | Configures Steam API endpoint for accessing app reviews. Defines URL base, parameters for number of reviews per page, language filter, and playtime filters.                                                                                                                                       |
| [APP_Hover_API.json](https://github.com/jameel978/Steam-Automation-Project/blob/master/Logic/Steam_API/API_Configs/APP_Hover_API.json)             | Navigate through Steams app hover functionality by making API requests to the designated endpoint with the provided configuration. This JSON file configures our Steam-API component, specifying the base URL for interacting with app hover functionalities on the Steam platform.                |
| [Advanced_search_API.json](https://github.com/jameel978/Steam-Automation-Project/blob/master/Logic/Steam_API/API_Configs/Advanced_search_API.json) | Configures advanced search parameters for the Steam API, enabling sorting by high or low price and hiding free games from results. URL, maximum price, language, sorting options, and game-type filters are customizable in this file.                                                             |
| [APP_Details_API.json](https://github.com/jameel978/Steam-Automation-Project/blob/master/Logic/Steam_API/API_Configs/APP_Details_API.json)         | URL for app details query, country code, and desired price information. This file drives Steam API interaction.                                                                                                                                                                                    |
| [Steam_token_API.json](https://github.com/jameel978/Steam-Automation-Project/blob/master/Logic/Steam_API/API_Configs/Steam_token_API.json)         | Interacting with Steam API configurations, this file defines the URL for accessing point summaries in the Steam stores AJAX interface. Essential for retrieving user points data within the projects broader automation framework.                                                                 |

</details>

<details closed><summary>.github.workflows</summary>

| File                                                                                                                   | Summary                                                                                                                                                                                                    |
| ---                                                                                                                    | ---                                                                                                                                                                                                        |
| [Test runner.yml](https://github.com/jameel978/Steam-Automation-Project/blob/master/.github/workflows/Test runner.yml) | In this GitHub workflow file, tests are orchestrated for the Steam-Automation-Project. It triggers various test scripts across API and website logic, ensuring code quality and functionality consistency. |

</details>

<details closed><summary>Utils</summary>

| File                                                                                                         | Summary                                                                                                                                                                                                                                               |
| ---                                                                                                          | ---                                                                                                                                                                                                                                                   |
| [requirements.txt](https://github.com/jameel978/Steam-Automation-Project/blob/master/Utils/requirements.txt) | Requests, Selenium, pytest, pytest-xdist, pytest-html, parameterized, pytest, allure-pytest, Jira library. This file plays a crucial role in ensuring a functional and well-equipped project environment.                                             |
| [Utils.py](https://github.com/jameel978/Steam-Automation-Project/blob/master/Utils/Utils.py)                 | Tests executed, 1 failed. Steam_website test case on Chrome failed in TestSuite. Output written to report.env file. Keep exploring new territories, we'll conquer the bugs.                                                                           |
| [Get_Cookies.py](https://github.com/jameel978/Steam-Automation-Project/blob/master/Utils/Get_Cookies.py)     | Collects cookies from multiple web browsers (chrome, edge, firefox) during login, saving them to a JSON file named tokens.json for later use within the repository.                                                                                   |
| [Create_Tokens.py](https://github.com/jameel978/Steam-Automation-Project/blob/master/Utils/Create_Tokens.py) | Generate tokens from environment variables and save as a JSON file named tokens.json. This utility script consolidates browser cookies, Jira tokens, project details, and run information into the configuration file for seamless project execution. |

</details>

<details closed><summary>Tests.Steam_website</summary>

| File                                                                                                                                           | Summary                                                                                                                                                                                                                                                                                                                               |
| ---                                                                                                                                            | ---                                                                                                                                                                                                                                                                                                                                   |
| [Steam_HomePage_test.py](https://github.com/jameel978/Steam-Automation-Project/blob/master/Tests/Steam_website/Steam_HomePage_test.py)         | Test case file for Steam HomePage searches in the Steam-Automation-Project. Imports required packages and sets up testing environment using BrowserWrapper and Home_page classes from Infra and Logic directories respectively. Runs tests on search functionality with different input parameters, asserting correctness of results. |
| [Wishlist_UI_API_test.py](https://github.com/jameel978/Steam-Automation-Project/blob/master/Tests/Steam_website/Wishlist_UI_API_test.py)       | Test script validates Steam wishlist functionality. Importantly, it integrates with both website UI and API using Infra components, ensuring wishlist games are added and removed as intended.                                                                                                                                        |
| [Cart_UI_API_test.py](https://github.com/jameel978/Steam-Automation-Project/blob/master/Tests/Steam_website/Cart_UI_API_test.py)               | Test script executes automated UI and API tests for Steams shopping cart functionality. Imports necessary dependencies, sets up test environment using browser and API wrappers, retrieves access token, runs add-to-cart test with API calls and verifies item presence in the cart.                                                 |
| [Search_Page_Search_test.py](https://github.com/jameel978/Steam-Automation-Project/blob/master/Tests/Steam_website/Search_Page_Search_test.py) | Test script executes searches on Steams website, verifying hide functionalities for wishlisted games and owned games, as well as price slider accuracy. It utilizes various infra components and API interfaces from both Logic and Infra packages to achieve desired test scenarios.                                                 |

</details>

<details closed><summary>Tests.Steam_website.Configs</summary>

| File                                                                                                                                                       | Summary                                                                                                                                                                                                                                                      |
| ---                                                                                                                                                        | ---                                                                                                                                                                                                                                                          |
| [Wishlist_UI_API_test.json](https://github.com/jameel978/Steam-Automation-Project/blob/master/Tests/Steam_website/Configs/Wishlist_UI_API_test.json)       | Configure test settings for API interactions with Steam websites wishlist feature in this file, providing app\_name" and app\_id values to target tests effectively.                                                                                         |
| [Search_Page_Search_test.json](https://github.com/jameel978/Steam-Automation-Project/blob/master/Tests/Steam_website/Configs/Search_Page_Search_test.json) | Owned game ID (730 for Counter-Strike 2), desired game name, and a filter for free games (-200).                                                                                                                                                             |
| [UI_Tests_Config.json](https://github.com/jameel978/Steam-Automation-Project/blob/master/Tests/Steam_website/Configs/UI_Tests_Config.json)                 | Chrome, Edge, and Firefox.                                                                                                                                                                                                                                   |
| [Cart_UI_API_test.json](https://github.com/jameel978/Steam-Automation-Project/blob/master/Tests/Steam_website/Configs/Cart_UI_API_test.json)               | Configures test parameters for a Steam game in the UI Automation tests. Defines app ID, bundle ID, and name for Mount & Blade Legacy Collection. Supporting accurate testing results within the Steam-Automation-Project infrastructure.                     |
| [Steam_HomePage_test.json](https://github.com/jameel978/Steam-Automation-Project/blob/master/Tests/Steam_website/Configs/Steam_HomePage_test.json)         | In the given repository, a JSON configuration file named `Steam_HomePage_test.json` exists within the `Configs` folder in the `Tests/Steam_website` directory. This file sets an application name for testing purposes in the Steam website automated tests. |

</details>

<details closed><summary>Tests.Steam_API</summary>

| File                                                                                                                                         | Summary                                                                                                                                                                                                                                                                                                               |
| ---                                                                                                                                          | ---                                                                                                                                                                                                                                                                                                                   |
| [test_app_review_api.py](https://github.com/jameel978/Steam-Automation-Project/blob/master/Tests/Steam_API/test_app_review_api.py)           | Test suite for Steam API app review functionality. Contains various test cases to verify getting app reviews, review numbers, language, and filtering reviews by minimum and maximum play time. Imports required modules from Infra and Logic layers. Uses unittest framework.                                        |
| [test_advanced_search_api.py](https://github.com/jameel978/Steam-Automation-Project/blob/master/Tests/Steam_API/test_advanced_search_api.py) | Tests advanced search functionality of Steam API. This file runs tests for sorting apps by price using `Advanced_search_API` and `APP_Details_API` classes from the Logic directory. It ensures returned results are not empty, prices are correctly sorted in descending or ascending order, and filters free games. |
| [test_app_details.py](https://github.com/jameel978/Steam-Automation-Project/blob/master/Tests/Steam_API/test_app_details.py)                 | This file implements unit tests for retrieving and validating app details using the ApiWrapper and APP\_Details\_API classes. Tests check getting app name and price currency for specified countries.                                                                                                                |
| [test_Store_Search_api.py](https://github.com/jameel978/Steam-Automation-Project/blob/master/Tests/Steam_API/test_Store_Search_api.py)       | This test suite verifies the correctness of Steams store search function. It initializes an instance of StoreSearchAPI and executes test cases to ensure the retrieved apps match expected results based on provided parameters, such as app names and IDs.                                                           |

</details>

<details closed><summary>Tests.Steam_API.Configs</summary>

| File                                                                                                                                                     | Summary                                                                                                                                                                                                                                                                                                    |
| ---                                                                                                                                                      | ---                                                                                                                                                                                                                                                                                                        |
| [test_app_review_api.json](https://github.com/jameel978/Steam-Automation-Project/blob/master/Tests/Steam_API/Configs/test_app_review_api.json)           | Configures test parameters for Steam APIs app review function in Tests/Steam_API/Configs/test_app_review_api.json". The file sets the app ID, desired language, and minimum and maximum play times for testing app reviews within the application.                                                         |
| [test_app_details.json](https://github.com/jameel978/Steam-Automation-Project/blob/master/Tests/Steam_API/Configs/test_app_details.json)                 | Configures app details for Steam API tests. In Tests/Steam_API/Configs folder, this JSON file stores the ID and name of the application to be tested (ELDEN RING with ID 1245620). Contribution to Steam-Automation-Project's test infrastructure.                                                         |
| [API_Tests_Config.json](https://github.com/jameel978/Steam-Automation-Project/blob/master/Tests/Steam_API/Configs/API_Tests_Config.json)                 | Configures test execution mode for parallel processing in Steam-API Tests within the repository.                                                                                                                                                                                                           |
| [test_Store_Search_api.json](https://github.com/jameel978/Steam-Automation-Project/blob/master/Tests/Steam_API/Configs/test_Store_Search_api.json)       | In our repositorys test configuration folder, a JSON file named test_Store_Search_api.json" exists. Its primary function is to store the application name, Elden Ring, for tests targeting Steam API functions. This configuration facilitates seamless test automation focusing on specific applications. |
| [test_advanced_search_api.json](https://github.com/jameel978/Steam-Automation-Project/blob/master/Tests/Steam_API/Configs/test_advanced_search_api.json) | Explore the `test_advanced_search_api.json` file in the `Tests/Steam-API/Configs` directory. This configuration file contains an application name, elden ring, which is utilized for advanced searches within the Steam API testing context in our project architecture.                                   |

</details>

---

##  Getting Started

**System Requirements:**

* **Python**: `version x.y.z`

###  Installation

<h4>From <code>source</code></h4>

> 1. Clone the Steam-Automation-Project repository:
>
> ```console
> $ git clone https://github.com/jameel978/Steam-Automation-Project
> ```
>
> 2. Change to the project directory:
> ```console
> $ cd Steam-Automation-Project
> ```
>
> 3. Install the dependencies:
> ```console
> $ pip install -r requirements.txt
> ```

###  Usage

<h4>From <code>source</code></h4>

> Run Steam-Automation-Project using the command below:
> ```console
> $ python main.py
> ```

###  Tests

> Run the test suite using the command below:
> ```console
> $ pytest
> ```

---

##  Project Roadmap

- [X] `► Add UI & API tests`
- [X] `► Add More Documentation (STP,STD,STR)`
- [ ] `► ...`

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/jameel978/Steam-Automation-Project/issues)**: Submit bugs found or log feature requests for the `Steam-Automation-Project` project.
- **[Submit Pull Requests](https://github.com/jameel978/Steam-Automation-Project/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/jameel978/Steam-Automation-Project/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/jameel978/Steam-Automation-Project
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="center">
   <a href="https://github.com{/jameel978/Steam-Automation-Project/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=jameel978/Steam-Automation-Project">
   </a>
</p>
</details>

---

##  License

This project is licensed under the [MIT License](LICENSE).

---


[**Return**](#-overview)

---
