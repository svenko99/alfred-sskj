# <img src='images/icon.png' width='45' align='absmiddle' alt='icon'>&nbsp;SSKJ Alfred Workflow

Look up definitions, synonyms, and word data in the Slovenian dictionary (SSKJ) – all from [Alfred](https://www.alfredapp.com/).

[**⤓ Download latest release**](https://github.com/svenko99/alfred-sskj/releases/latest/download/SSKJ.alfredworkflow) or get it from the [Alfred Gallery](https://alfred.app/workflows/svenko99/sskj/).

![Looking up a word](images/example.gif)

## Usage

### Definitions

Look up the definitions of a word via the `sskj` keyword, e.g. `sskj krog`.

* <kbd>↩&#xFE0E;</kbd> Copy the definition.
* <kbd>⌥</kbd><kbd>↩&#xFE0E;</kbd> Open the word on [fran.si](https://fran.si/).

### Synonyms

Look up the synonyms of a word via the `sinonim` keyword, e.g. `sinonim čas`.

* <kbd>↩&#xFE0E;</kbd> Copy the synonym.
* <kbd>⌥</kbd><kbd>↩&#xFE0E;</kbd> Open the word in the synonym dictionary on [fran.si](https://fran.si/).

### Word data

Look up the word type and gender via the `podatki` keyword, e.g. `podatki krog`. Every matching entry is listed, so `krog` shows both the noun and the preposition.

* <kbd>↩&#xFE0E;</kbd> Copy the word data.
* <kbd>⌥</kbd><kbd>↩&#xFE0E;</kbd> Open the entry on [Sloleks](https://viri.cjvt.si/sloleks/slv/).

### Word suggestions

Get real-time word suggestions as you type via the `iskanje` keyword, e.g. `iskanje kro`. Press <kbd>⇥</kbd> to autocomplete a suggestion.

* <kbd>↩&#xFE0E;</kbd> Show definitions.
* <kbd>⌘</kbd><kbd>↩&#xFE0E;</kbd> Show synonyms.
* <kbd>⌃</kbd><kbd>↩&#xFE0E;</kbd> Show word data.
* <kbd>⌥</kbd><kbd>↩&#xFE0E;</kbd> Open the word on [fran.si](https://fran.si/).

In definitions, synonyms, and word data, <kbd>⇧</kbd> opens a Quick Look preview and <kbd>⌘</kbd><kbd>L</kbd> shows the full text in Large Type – handy for long definitions.

## Requirements

[uv](https://docs.astral.sh/uv/getting-started/installation/) must be installed. On first run it sets up Python and the dependencies automatically. The workflow looks for `uv` in `~/.local/bin`, `/opt/homebrew/bin`, and `/usr/local/bin`.

Data comes from [fran.si](https://fran.si/) (SSKJ² and Sinonimni slovar) and [Sloleks](https://viri.cjvt.si/sloleks/slv/).

## License

[MIT](./LICENSE)
