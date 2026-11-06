"""Builds the AACN session site: one overview page plus three tool-guide pages.

Edit page content below, then run `python3 build.py`.
Output: index.html and step-N/index.html (N = 1-3).
"""
from pathlib import Path

ROOT = Path(__file__).parent

TITLE = "Detection to documentation"
SUBTITLE = "Using “Revision History” tool to support authentic writing through process-based assessment"
EVENT = "AACN Transform 2026 · Podium presentation · Friday, Dec. 4, 9:25–9:45 a.m. · Indianapolis"
SITE_URL = "https://briannapack.github.io/detection-to-documentation-aacn/"
OLC_URL = "https://briannapack.github.io/detection-to-documentation/"

TOOL_STEPS = [
    ("s1", "step-1/", "1", "Install the extension"),
    ("s2", "step-2/", "2", "Read the history"),
    ("s3", "step-3/", "3", "Watch the replay"),
]

HOME_NAV = [
    ("why", "Why it matters"), ("show", "SHOW"), ("writing", "Writing course"), ("group", "Group project"),
    ("compare", "Side by side"), ("yours", "Your course"), ("tool", "Learn the tool"),
]


def video(base, file, poster, label, length, captions):
    lines = "".join(f"<li>{c}</li>" for c in captions)
    return f"""<figure class="vid">
<video controls playsinline preload="metadata" poster="{base}assets/img/{poster}" aria-label="{label}">
<source src="{base}assets/video/{file}" type="video/mp4"></video>
<figcaption class="small">{length} · silent with captions on screen</figcaption>
<details class="col"><summary>Read the on-screen captions</summary><ol class="caps">{lines}</ol></details>
</figure>"""


def badge(base, letter, size=56):
    return f'<img class="badge" src="{base}assets/img/badge-{letter}.png" alt="{letter}" width="{size}" height="{size}">'


SHOW_ROWS = [
    ("S", "Structure the assignment", "Milestones in one shared Google Doc. You’re an editor, all writing happens in the Doc, and students submit the link."),
    ("H", "Hold students accountable", "At the first milestone, check the history for pasting and for anyone not taking part. Accountability, not grading."),
    ("O", "Observe and respond", "Formative feedback at each milestone. Students revise in the same Doc, so the history shows their growth."),
    ("W", "Weigh the whole picture", "Grade development, revision and participation, not only the final product."),
]

COMPARE = [
    ("S", "Structure", "Drafts of one statement in one individual Doc, shared with faculty as Editor",
     "Milestones for data, analysis and report in one group Doc"),
    ("H", "Hold accountable", "Large pastes earn a zero", "No pasting, and every member contributes"),
    ("O", "Observe and respond", "Comments on drafts, then revision in the Doc", "Feedback on survey questions, then revision in the Doc"),
    ("W", "Weigh the whole picture", "The history confirms authorship and growth", "Credit for each member’s part"),
]

REPLAY_CAPTIONS = [
    "Does this look like real writing?", "Real writing starts, stops, and gets revised.", "Speed changes from 1x to 2x.",
    "Two authors, each typing in bursts.", "Each author’s share of the text.", "Work happened over several sittings.",
    "Large pastes are listed with times.", "Pastes are marked on the timeline too.", "Yellow: pasted from outside the document.",
    "Green: their own text, moved. Usually fine.", "Labels are estimates, so use them as a prompt.", "Click any paste to see it happen.",
    "Or click its marker on the timeline.", "The text keeps growing a little at a time.", "Slow it to 0.25x.",
    "Jump back to just before the paste.", "Typed text builds up gradually.", "This appeared all at once.",
    "A sudden block of text is a reason to ask the student. Try it on your own Google Doc.",
]

SHOW_CAPTIONS = [
    "How do you make your students SHOW their work?", "A group project set up with SHOW.",
    "“Add me as an editor when your group creates this Google Doc.” Instructor sees every draft.",
    "“Do all writing directly in the Google Doc.” No pasting means a visible process.",
    "“Looking Ahead: This brainstorm is the first draft of your project proposal.” Feedback comes before the final version.",
    "“Submit the Google Doc shareable link in the Canvas submission box.” Only the original Doc keeps its history.",
    "From detection to documentation: the process is the evidence. Try it: redesign one assignment with SHOW.",
]

INSTALL_CAPTIONS = [
    "How do you add Revision History to Chrome?", "Type revisionhistory.com into Chrome.", "Click Get Extension.",
    "Click Add to Chrome.", "Approve it: click Add extension.", "Click the puzzle piece.",
    "Pin Revision History. The pin turns blue.", "Open any Google Doc.", "Click Sign in with Google in the new bar.",
    "Sign in with Google.", "Once you’re signed in, this bar appears.",
    "You’re set up. Next: Step 2, read the history.",
]

HISTORY_CAPTIONS = [
    "What can a document’s history tell you?", "Open Version history: click the clock icon.",
    "This is Google Docs’ built-in Version history.", "Version history shows who wrote each part, and when.",
    "Click an earlier version to see one person’s edit, in their color.",
    "The next version: a whole paragraph at once. You see the stage, not how it got there.",
    "The Revision History extension adds how: keystrokes, sessions, and pastes.", "Pastes from outside the doc.",
    "Writing sessions and total writing time.", "Click Details to see more.",
    "Editing sessions: when, and for how long.", "Large pastes: what was pasted, and when.",
    "Two tools, one approach: look at the process. Next: Step 3, watch the replay.",
]


def tool_cards(b):
    return "".join(f'<a class="tcard" href="{b}{p}"><span class="num">{n}</span><span>{t}</span></a>' for _, p, n, t in TOOL_STEPS)


def home(b):
    show = "".join(f'<div class="srow">{badge(b, l)}<div><h3>{t}</h3><p>{d}</p></div></div>' for l, t, d in SHOW_ROWS)
    comp = "".join(f'<tr><th scope="row">{badge(b, l, 40)}<span>{n}</span></th><td>{w}</td><td>{g}</td></tr>' for l, n, w, g in COMPARE)
    return f"""
<section class="sec" id="why"><div class="in narrow">
<p class="eyebrow">Why it matters in nursing education</p>
<h2 class="title">If it wasn’t documented, it wasn’t done</h2>
<p class="lead">Nurses learn early that documentation is part of the care. We ask students to document what they do for patients. This session asks: what if they documented their writing process too?</p>
<p>AI detectors guess from the final product, and they flag some students far more than others, including non-native English writers, with emerging evidence of more false flags for neurodivergent students (Liang et al., 2023; Eaton, 2025). Many nursing students are multilingual, and a false flag can put a student’s place in the program at risk. Documentation is different: it shows how the work developed, and it starts a conversation instead of an accusation.</p>
<p>The free ‘Revision History’ extension for Chrome reads the edit history Google Docs already keeps: writing time, every paste, who wrote what, and a replay. It isn’t an AI detector. It shows the process, and you make the call.</p>
</div></section>

<section class="band" id="show"><div class="in narrow">
<p class="eyebrow">The approach</p>
<h2 class="title">Make your students SHOW their work</h2>
<p class="lead">Four steps to redesign a writing assignment around the process, in any nursing course and any modality.</p>
<div class="show">{show}</div>
</div></section>

<section class="sec" id="writing"><div class="in narrow">
<p class="eyebrow">Example 1 · One student, one Doc</p>
<h2 class="title">Writing course: a teaching statement</h2>
<p>Most of the work of SHOW happens in the assignment instructions. Here are Sharon Titus’s submission instructions for an individual teaching statement in her nursing course. They set up S and H before a single word is written.</p>
<div class="instr"><p class="ihead">How to submit (follow these steps in order)</p>
<ol><li><b>Create a new Google Doc.</b> Title it LastName_FirstName_Teaching Statement.</li>
<li><b>Share it with your faculty as Editor.</b> Click the blue Share button, enter your faculty’s email, change the role from Viewer to Editor, and click Send. Viewer or Commenter access will prevent grading and will be treated as a missed submission.</li>
<li><b>Submit the URL in Canvas by Wednesday.</b> Paste the link into the text-entry box. Confirm it works by opening it in a private browser window, or ask a classmate to test it.</li>
<li><b>Write your statement directly in the Google Doc.</b> Do all drafting, revising, and analysis in this document from start to finish.</li></ol>
<p class="ihead">Important submission rules</p>
<ul><li>Do not download your document as a Word file or PDF and upload it to Canvas. Only the shared Google Doc link will be accepted.</li>
<li>Your instructor will grade directly in your Google Doc and review the revision history to confirm authorship.</li>
<li><b>Large copied, pasted, or imported content will receive a grade of 0.</b> This includes text pasted from another document, a website, or an AI tool.</li>
<li>Do not change sharing permissions or edit the document after the deadline unless instructed.</li></ul></div>
<p class="note"><b>Expect some pushback, and read it as a good sign.</b> Students who don’t like writing in the Doc are often reacting to the fact that they now have to do the work themselves.</p>
</div></section>

<section class="band" id="group"><div class="in narrow">
<p class="eyebrow">Example 2 · A group, one shared Doc</p>
<h2 class="title">Group project: an applied data course</h2>
<p>Brianna Pack teaches statistics in the undergraduate nursing program. Students gather real-world data and run the analysis as a group, and the report is built milestone by milestone in one shared Google Doc. Groups add two things the history can show: who participated, and who wrote what.</p>
{video(b, 'make-your-students-show-their-work.mp4', 'poster-show.jpg', 'Video: a group project set up with SHOW', '59 seconds', SHOW_CAPTIONS)}
<p class="note">After the standard was set at the first milestone, very few students pasted on the next assignment, and group participation improved. When a paste did show up, it started a conversation, not an accusation.</p>
</div></section>

<section class="sec" id="compare"><div class="in">
<p class="eyebrow">Same approach, different courses</p>
<h2 class="title">Side by side</h2>
<div class="tablewrap"><table class="cmp"><thead><tr><th scope="col"><span class="sr">SHOW step</span></th><th scope="col">Writing course: individual teaching statement</th><th scope="col">Applied course: group data project</th></tr></thead>
<tbody>{comp}</tbody></table></div>
<p class="modal"><b>Any modality.</b> Face-to-face, hybrid or online: almost every course runs its written work online now, so wherever the writing happens in a shared Doc, SHOW applies. That includes clinical and simulation coursework, like reflections and care plans.</p>
</div></section>

<section class="band" id="yours"><div class="in narrow">
<p class="eyebrow">Now your course</p>
<h2 class="title">Redesign one assignment</h2>
<p class="try">Think of a writing assignment where you couldn’t be sure the work was the student’s own. Is it closer to the writing course or the group project? Start from that column, and add one SHOW step at a time.</p>
<details class="col"><summary>Sample assignment language you can paste in</summary>
<ol class="copy"><li><b>Add me as an editor when you create this Google Doc.</b> I use the revision history to verify participation and authorship and ensure fairness. Students who do not show active involvement in the Google Doc will not receive credit.</li>
<li><b>Do all writing directly in the Google Doc.</b> The revision history is how I see your writing process, and the process is part of what this assignment asks for. Content that is written elsewhere and pasted, imported, or uploaded into the document cannot be verified, so it will receive a zero.</li></ol>
<p><b>To submit:</b> Share the Doc with your faculty as Editor, and submit the Google Doc’s link in Canvas. Do not upload a Word or PDF copy.</p>
<button class="copybtn" type="button">Copy this language</button></details>
<h3 class="h3">Know the limits</h3>
<ul class="limits"><li><b>Pasting from elsewhere.</b> Students can draft in another file and paste it in, so some authorship can’t be verified. Treat a paste as a reason to ask, and set the expectation at the first milestone.</li>
<li><b>Internet access.</b> Composing in Google Docs needs a steady connection, which can disadvantage some students. Build in flexible milestones.</li>
<li><b>Infrastructure.</b> Google Workspace and Chrome extensions aren’t standard in every nursing program. The SHOW approach still works with any tool that keeps a version history.</li></ul>
<h3 class="h3">Connections to the AACN Essentials</h3>
<p>Process-based assessment supports Domain 9, Professionalism (accountability and integrity), and Domain 8, Informatics and Healthcare Technologies. Documenting, revising and owning your work are habits of nursing practice.</p>
</div></section>

<section class="sec" id="tool"><div class="in narrow">
<p class="eyebrow">Learn the tool</p>
<h2 class="title">Three short videos</h2>
<p>Each video is about a minute, silent with captions, and shows the tool on a real Google Doc. Follow along on your own Doc whenever you’re ready.</p>
<div class="tcards">{tool_cards(b)}</div>
</div></section>"""


def tool_page(b, key, title, vid, lead, tryit, nxt):
    nav = "".join(f'<a href="{b}{p}"{" aria-current=\"page\"" if k == key else ""}><span>Video {n}</span>{t}</a>' for k, p, n, t in TOOL_STEPS)
    nxt_html = (f'<a class="btn" href="{b}{nxt[0]}">{nxt[1]} <span aria-hidden="true">→</span></a>' if nxt else
                f'<a class="btn" href="{b}#yours">Now redesign your assignment <span aria-hidden="true">→</span></a>')
    return f"""
<nav class="toolnav" aria-label="Tool videos"><div class="in"><a class="back" href="{b}#tool">← Overview</a>{nav}</div></nav>
<section class="sec"><div class="in narrow"><p class="eyebrow">Learn the tool</p><h2 class="title">{title}</h2>
{vid}
<p class="lead">{lead}</p>
<div class="trybox"><p class="lbl">Try it</p><p>{tryit}</p></div>
<p class="center">{nxt_html}</p></div></section>"""


def step1(b):
    return tool_page(b, "s1", "Install the extension",
                     video(b, 'install-the-extension.mp4', 'poster-install.jpg', 'Video: Install the extension', '1 minute 6 seconds', INSTALL_CAPTIONS),
                     "Add the free ‘Revision History’ extension to Chrome, pin it, and sign in, so you can see the history of your own Google Docs.",
                     "In Chrome, go to <b>revisionhistory.com</b> and click <b>Add to Chrome</b>. Pin it to your toolbar, open any Google Doc, and click <b>Sign in with Google</b> in the bar at the top.",
                     ("step-2/", "Next: read the history"))


def step2(b):
    return tool_page(b, "s2", "Read a document’s history",
                     video(b, 'read-the-history.mp4', 'poster-history.jpg', 'Video: Read a document’s history', '1 minute 8 seconds', HISTORY_CAPTIONS),
                     "Start with Google Docs’ built-in version history to see who wrote each part and when. Then open the extension’s Details to add how it was written: keystrokes, sessions, writing time, and pastes.",
                     "Open a Google Doc you’ve written over a few sittings. Click the <b>clock icon</b> at the top right to open Version history, then click <b>Details</b> in the Revision History bar.",
                     ("step-3/", "Next: watch the replay"))


def step3(b):
    return tool_page(b, "s3", "Watch a document being written",
                     video(b, 'watch-a-document-being-written.mp4', 'poster-replay.jpg', 'Video: Watch a document being written', '1 minute 54 seconds', REPLAY_CAPTIONS),
                     "Replay a two-author document, find the pastes, and slow down to see what typed writing looks like next to text that appears all at once.",
                     "In your own Google Doc, click <b>Watch Replay</b> in the Revision History bar. Try a faster speed, and if your Doc has any pastes, click a paste marker to jump to that moment.",
                     None)


PAGES = [
    ("home", "", "Overview", home),
    ("s1", "step-1/", "Install the extension", step1),
    ("s2", "step-2/", "Read the history", step2),
    ("s3", "step-3/", "Watch the replay", step3),
]


def page(key, path, name, body):
    b = "../" if path else ""
    homenav = ""
    if key == "home":
        homenav = '<nav class="secnav" aria-label="On this page"><div class="in">' + "".join(
            f'<a href="#{i}">{t}</a>' for i, t in HOME_NAV) + "</div></nav>"
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{name} · {TITLE}</title>
<meta name="description" content="{SUBTITLE}. SHOW across nursing courses, from AACN Transform 2026.">
<meta property="og:title" content="{TITLE}: {name}"><meta property="og:description" content="{SUBTITLE}. Nursing education, any modality.">
<meta property="og:url" content="{SITE_URL}{path}"><meta property="og:image" content="{SITE_URL}assets/img/share.png">
<meta property="og:image:alt" content="{TITLE}: {SUBTITLE}"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{b}assets/img/badge-S.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;600;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{b}assets/site.css"></head>
<body><a class="skip" href="#main">Skip to content</a>
<header class="hero"><div class="in">
<div class="toprow"><img class="apu" src="{b}assets/img/apu-white.png" alt="Azusa Pacific University" width="179" height="40"></div>
<h1><a href="{b}">{TITLE}</a></h1><p class="sub">{SUBTITLE}</p>
<p class="meta">{EVENT}<br>Sharon K. Titus, PhD, MSN, RN, and Brianna M. Pack, MPH, MBA, College of Nursing &amp; Health Sciences</p></div></header>
{homenav}
<main id="main">{body(b)}
<section class="take"><div class="in narrow">
<div class="takegrid"><div><h2 class="h3">Take it with you</h2><p><a href="{b}downloads/Detection-to-Documentation-Slides.pdf" target="_blank" rel="noopener">View the slides (PDF)</a></p></div>
<div><h2 class="h3">Also presented at OLC Accelerate 2026</h2><p>The <a href="{OLC_URL}">OLC version</a> applies the same approach to online teaching across disciplines, with a hands-on walkthrough.</p></div></div>
<details class="col refs"><summary>References</summary><ul>
<li>American Association of Colleges of Nursing. (2021). <i>The Essentials: Core competencies for professional nursing education</i>. https://www.aacnnursing.org/essentials</li>
<li>Eaton, S. E. (2025). Neurodiversity and academic integrity: Toward epistemic plurality in a postplagiarism era. <i>Teaching in Higher Education</i>. https://doi.org/10.1080/13562517.2025.2583456</li>
<li>Gay, K., &amp; Muscanell, N. (2026, March 23). <i>2026 EDUCAUSE students and technology report: Steady through change</i>. EDUCAUSE.</li>
<li>Liang, W., Yuksekgonul, M., Mao, Y., Wu, E., &amp; Zou, J. (2023). GPT detectors are biased against non-native English writers. <i>Patterns, 4</i>(7), Article 100779. https://doi.org/10.1016/j.patter.2023.100779</li>
<li>Schmitz, A., &amp; Laird, E. (2025, December). AI-powered pedagogy: A guide to evidence-based teaching tools. <i>EDUCAUSE Review</i>.</li>
<li>Revision History. (n.d.). <i>Writing process visibility for Google Docs &amp; Slides</i>. https://revisionhistory.com</li></ul></details>
</div></section></main>
<footer class="foot"><p class="names">Sharon K. Titus, PhD, MSN, RN (<a href="mailto:stitus@apu.edu">stitus@apu.edu</a>) · Brianna M. Pack, MPH, MBA (<a href="mailto:bpack@apu.edu">bpack@apu.edu</a>) · Azusa Pacific University</p>
<p>Educational session at AACN Transform 2026. ‘Revision History’ is a third-party tool shown for teaching; its mention here isn’t an endorsement, and the presenters have no affiliation with it.</p>
<p>AI use: Claude (Anthropic) helped draft and edit this site, the slides and the videos. The presenters reviewed all content.</p></footer>
<script src="{b}assets/site.js" defer></script>
</body></html>
"""


if __name__ == "__main__":
    for key, path, name, body in PAGES:
        out = ROOT / path / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page(key, path, name, body))
        print("wrote", out.relative_to(ROOT))
