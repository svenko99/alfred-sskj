# 📖 SSKJ workflow for Alfred

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![macOS](https://svgshare.com/i/ZjP.svg)](https://svgshare.com/i/ZjP.svg)
## 🤔 What is it?
- It's Alfred workflow for quickly	looking up **definition** of certain word in Slovenian dictionary - SSKJ *(Slovar slovenskega knjižnega jezika)*
- It can also be used to find **synonyms** of certain word
- It's using data from websites [**termania.net**](https://www.termania.net/) and [**sinonimi.si**](https://sinonimi.si/)
- Workflow is written in **Python 3.11**

## Installation
- Workflow depends on two package, namely [requests](https://pypi.org/project/requests/) and [beautifulsoup4](https://pypi.org/project/beautifulsoup4/), hance 
 you need to install it before using this workflow:

	- ```pip3 install requests beautifulsoup4```


- after that the only thing  left is to install [SSKJ.alfredworkflow](https://github.com/svenko99/alfred-sskj/raw/main/SSKJ.alfredworkflow) in the repo


## Usage
- In Alfred type `sskj` and your word of choice e.i. `sskj krog` or `sskj pica`
- If you hit enter the definition of the word will be copied to the clipboard
- To get synonyms of word type `sinonim` and your word of choice e.i. `sinonim krog` or `sinonim čas`

	<img src="https://user-images.githubusercontent.com/107575361/200019676-20371147-4eb0-4f9b-9f8b-130c1df930b7.gif" width=80% height=80%/>
