# Website Information Tool

This Project Allows Users To Gather Detailed Information About A Website Through A Simple Terminal Interface. By Interacting With The Website's URL, The Script Provides Various Functionalities To Test, Retrieve, And Analyze The Site's Resources And Response.

## Features

The Tool Provides The Following Features:

1. **Show URL**: Displays The URL of The Website.
2. **Test Connection**: Verifies If The Website Is Accessible And Its Connection Is Working Properly.
3. **Get 'robots.txt'**: Retrieves The `robots.txt` File To Check For Any Crawl Restrictions.
4. **Get Source Code**: Fetches The Raw HTML Source Code of The Website.
5. **Get Links**: Lists All The Links (URLs) Present On The Website.
6. **Get Text**: Extracts And Displays The Visible Text Content From The Website.
7. **Get Response Time**: Displays The Response Time of The Website.
8. **Check For Certifications**: Checks If The Website Has Any Ssl Certificates Installed.
9. **Check For Cookies**: Checks If The Website Sets Any Cookies.

## Requirements

To Run This Project, You Need To Have Python Installed Along With The Following Dependencies:

- `minerpy` Library (For Interacting With The Website).

You Can Install The Required Dependencies With The Following Command:

```bash
pip Install Minerpy
```

## Usage

1. Clone or Download The Repository.
2. Open A Terminal And Run The Python Script.
3. You Will Be Prompted To Enter The URL of The Website You Want To Inspect.
4. After Entering The Website URL, You Will Be Presented With A Menu of Available Actions To Choose From.

### Sample Usage:

```bash
Enter Website
> https://example.com

1> Show URL
2> Test Connection
3> Get 'robot.txt'
4> Get Source Code
5> Get Links
6> Get Text
7> Get Response Time
8> Check For Certifications
9> Check For Cookies
> 1

Website: https://example.com
```

Select The Corresponding Number From The Menu To Perform The Desired Action. For Example:

- Enter `1` To Show The Website's URL.
- Enter `4` To Get The Source Code of The Website.

### Example of Available Actions:

- **Get 'robots.txt'**: Fetches The Robots.txt File From The Website, Which May Contain Rules For Web Crawlers.
- **Test Connection**: Verifies If The Website Is Reachable or Not By Attempting To Establish A Connection.
- **Get Response Time**: Measures How Long It Takes For The Website To Respond To A Request.

## Contributing

Feel Free To Fork The Project, Create A Branch, And Submit Pull Requests. Contributions Are Welcome!

- The Project Uses The `minerpy` Library For Site Analysis.

---
