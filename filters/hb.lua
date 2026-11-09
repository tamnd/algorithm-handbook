-- The filter of the handbook (spec handbook 04.4).
-- One Markdown source serves LaTeX and EPUB. This filter maps the marks of hb/prep.py onto each target:
--   class html-only          the element is dropped from LaTeX
--   Div  latex-env=NAME      LaTeX: \begin{NAME}[{latex-arg}] … \end{NAME}
--   Span latex-cmd=NAME      LaTeX: \NAME{…}
--   Span .ref                LaTeX: \hbref{…}, the number of an entry after a link
--   CodeBlock .plain         LaTeX: the hbverbatim environment (breaks long lines, keeps the fallback fonts)

local is_latex = FORMAT:match("latex") ~= nil

local function has(el, c)
  for _, x in ipairs(el.classes or {}) do if x == c then return true end end
  return false
end

local function texarg(s)
  return (s:gsub("([\\{}$&#^_%%~])", "\\%1"))
end

function Div(el)
  if is_latex and has(el, "html-only") then return {} end
  local env = el.attributes["latex-env"]
  if is_latex and env then
    local arg = el.attributes["latex-arg"]
    local open = "\\begin{" .. env .. "}" .. (arg and ("{" .. texarg(arg) .. "}") or "")
    local out = {}
    if el.identifier ~= "" then
      table.insert(out, pandoc.RawBlock("latex", "\\phantomsection\\label{" .. el.identifier .. "}"))
    end
    table.insert(out, pandoc.RawBlock("latex", open))
    for _, b in ipairs(el.content) do table.insert(out, b) end
    table.insert(out, pandoc.RawBlock("latex", "\\end{" .. env .. "}"))
    return out
  end
  if not is_latex then
    el.attributes["latex-env"] = nil
    el.attributes["latex-arg"] = nil
    return el
  end
end

function Header(el)
  if is_latex and has(el, "html-only") then return {} end
  if not is_latex then
    el.classes = el.classes:filter(function(c) return c ~= "html-only" end)
    return el
  end
end

function Para(el)
  -- a paragraph that is only an html-only span (the kind badge) goes away in LaTeX
  if is_latex and #el.content == 1 and el.content[1].t == "Span" and has(el.content[1], "html-only") then
    return {}
  end
end

function Span(el)
  if is_latex and has(el, "html-only") then return {} end
  local cmd = el.attributes["latex-cmd"]
  if is_latex and cmd then
    local out = { pandoc.RawInline("latex", "\\" .. cmd .. "{") }
    for _, x in ipairs(el.content) do table.insert(out, x) end
    table.insert(out, pandoc.RawInline("latex", "}"))
    return out
  end
  if is_latex and has(el, "ref") then
    return { pandoc.RawInline("latex", "\\hbref{" .. pandoc.utils.stringify(el.content) .. "}") }
  end
  if not is_latex then
    el.attributes["latex-cmd"] = nil
    return el
  end
end

function CodeBlock(el)
  if is_latex and has(el, "plain") then
    -- hbverbatim has commandchars \ { }, so that \hbfb works inside it; escape the three
    local t = el.text:gsub("[\\{}]", { ["\\"] = "\\textbackslash{}", ["{"] = "\\{", ["}"] = "\\}" })
    return pandoc.RawBlock("latex", "\\begin{hbverbatim}\n" .. t .. "\n\\end{hbverbatim}")
  end
end
