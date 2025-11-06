//Themes
- C/C++ Themes
- Winter is coming
- codeSTACKr
- Night owl
- Palenight / Material Theme Palenight
- One Dark Pro
- Ayu Dark
- Custom ChatGPT Theme
    - Night Owl Theme install
    - Material Icon Theme
    - Fira Code (Font)
    - Create settings.json
    {
  // UI THEME
  "workbench.colorTheme": "Night Owl",
  "workbench.iconTheme": "material-icon-theme",

  // EDITOR LOOK & FEEL
  "editor.fontFamily": "Fira Code, JetBrains Mono, Consolas, 'Courier New', monospace",
  "editor.fontLigatures": true,
  "editor.fontSize": 14,
  "editor.lineHeight": 22,

  // COLORS — tuned to match your screenshot
  "workbench.colorCustomizations": {
    "editor.background": "#011627",       // deep navy background (Night Owl base)
    "editorCursor.foreground": "#80CBC4",  // soft teal cursor
  },

  // SYNTAX COLOR TWEAKS — more contrast like in screenshot
  "editor.tokenColorCustomizations": {
    "[Night Owl]": {
      "textMateRules": [
        {
          "scope": ["keyword"],
          "settings": { "foreground": "#FF6363" }  // pink/red keywords (return, if, def)
        },
        {
          "scope": ["entity.name.function", "support.function"],
          "settings": { "foreground": "#82AAFF" }  // blue functions
        },
        {
          "scope": "entity.other.attribute-name",
          "settings": { "foreground": "#7FDBCA" }  // bright cyan decorators (@property)
        },
        {
          "scope": ["string", "constant.other"],
          "settings": { "foreground": "#E2C08D" }  // yellow strings / named args
        }
      ]
    }
  }
}

//Python
- autopep8, formatter python
- Python
- Pytohn debugger

//C++
- C/C++
- C/C++ extension pack
- CMake
- Cmake tools

//Docker
- Container tools
- Docker
- Docker explorer


//Other
- PlatformIO
- Remote SSH
- Remote SSH: Editing Configuration files
- Remote Exlorer
- GitLens
- Code Spell Checker
- Error Lens
- Material Icon
- Live server
- Github copilot chat
- Github copilot chat
