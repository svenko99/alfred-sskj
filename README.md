# 📖 SSKJ workflow for Alfred

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![macOS](https://svgshare.com/i/ZjP.svg)](https://svgshare.com/i/ZjP.svg)
## 🤔 What is it?
- It's Alfred workflow for quickly	looking up **definition** of certain word in Slovenian dictionary - SSKJ *(Slovar slovenskega knjižnega jezika)*
- It's using data from webiste [Fran.si](https://fran.si/)
- Workflow is written in **Python 3.10**

## Installation
- Workflow depends on two package, namely [requests](https://pypi.org/project/requests/) and [beautifulsoup4](https://pypi.org/project/beautifulsoup4/), hance 
 you need to install it before using this workflow:

	- ```pip3 install requests beautifulsoup4```


- after that the only thing  left is to install [sskj.alfredworkflow](https://github.com/svenko99/alfred-sskj/raw/main/sskj.alfredworkflow) in the repo


## Usage
- In Alfred type `sskj` and your word of choice e.i. `sskj krog` or `sskj pica`
- If you enter the definition of the word will be copied to the clipboard

![Screenshot 2022-09-22 at 09 32 09 2](https://user-images.githubusercontent.com/107575361/191687377-c7c328ef-e42d-4857-b931-51405d455267.jpeg)
