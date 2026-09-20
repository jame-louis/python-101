// Site metadata — the only non-content configuration.
// Everything else (navigation labels, lectures, assignments) lives in Markdown under src/content/.
export const site = {
  lang: 'zh-CN',
  title: 'Python 101', // Course/site name shown in header + footer — edit to rename the site
  description: 'Python语言基础语法与机器学习入门', // One-line description shown in the homepage header + meta
  term: '2026 秋季学期', // Shown as a meta line in the homepage header — edit or remove for your semester
  separator: ' · ',
} as const;
