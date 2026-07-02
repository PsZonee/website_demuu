import os

ROOT = os.path.dirname(os.path.abspath(__file__))
CH_DIR = os.path.join(ROOT, "chapters")

# ---------------------------------------------------------------------------
# Content
# ---------------------------------------------------------------------------

CHAPTERS = [
    {
        "title": "The Message",
        "subtitle": "Instagram, the beginning",
        "eyebrow": "chapter one",
        "paras": [
            "It started the way nothing important is supposed to start — with a message about project work. You needed help. I said okay. That was the whole plan.",
            "I didn't know that \"okay\" was going to become the most important word I ever typed. I didn't know I was replying to a text and also, somehow, to the rest of my life.",
            "We talked about the project for a while. Then we talked about everything else. The project ended. We didn't.",
        ],
    },
    {
        "title": "The Project That Wasn't Really About the Project",
        "subtitle": "how a favor turned into us",
        "eyebrow": "chapter two",
        "paras": [
            "I still laugh thinking about it — two people pretending to focus on slides and deadlines while actually just finding reasons to keep texting.",
            "Every reply took a little longer to send, because I kept rewriting it so it sounded less like homework and more like I wanted to know you.",
            "Somewhere between the notes and the messages, the project became the excuse and you became the reason.",
        ],
    },
    {
        "title": "Notes I Fell For",
        "subtitle": "your handwriting, my captions",
        "eyebrow": "chapter three",
        "paras": [
            "I liked your notes before I even understood why. Something about the way you explained things — careful, unshowy, yours.",
            "And you liked mine back — the notes, the pictures, the little stories I put up without thinking too hard about them. You paid attention. That's rare.",
            "We were two people quietly impressed by each other's ordinary days, before either of us said it out loud.",
        ],
    },
    {
        "title": "Everything I Told You",
        "subtitle": "sharing our pasts",
        "eyebrow": "chapter four",
        "paras": [
            "At some point the conversation stopped being light. We started telling each other the real things — where we'd been, what had hurt, who we used to be before this.",
            "You listened to my past without flinching. I listened to yours the same way. Neither of us tried to edit the other into someone easier to love.",
            "That's when I knew this wasn't just talking anymore. It was trust, arriving quietly, one honest story at a time.",
        ],
    },
    {
        "title": "June 6th",
        "subtitle": "the day it became official",
        "eyebrow": "chapter five",
        "paras": [
            "June 6, 2025. I remember it the way you remember a date that quietly rearranges your whole calendar around it.",
            "One day we were two people who talked a lot. The next, we were <em>us</em> — with a start date, a story, and a reason to celebrate the sixth of every month like it's still new.",
            "It wasn't a big dramatic moment. It was just two people finally saying the thing we'd both already decided. And it was enough to change everything.",
        ],
    },
    {
        "title": "The Names You Wear",
        "subtitle": "Prashi, baby, punti, bauni, Prashu",
        "eyebrow": "chapter six",
        "paras": [
            "You have more names than most people, and I use every single one on purpose.",
            "<strong>Prashu</strong> when I'm just talking to you. <strong>Prashi</strong> when I'm being soft about it. <strong>Baby</strong> when I miss you mid-sentence. <strong>Punti</strong> and <strong>Bauni</strong> when nothing else fits the mood and only nonsense will do.",
            "None of the names are your real one, and somehow all of them are exactly you. I think that's what love does — it gives a person more names than they started with, because one was never going to be enough.",
        ],
    },
    {
        "title": "Kutta",
        "subtitle": "the one name only you get to call me",
        "eyebrow": "chapter seven",
        "paras": [
            "You call me <em>kutta</em> and somehow it lands softer than any pet name I've ever heard.",
            "It shouldn't work. On paper it's an insult. In your voice it's an entire relationship — teasing, familiar, safe enough to be silly in.",
            "I let you call me whatever you want, because I know exactly what it means underneath the word. It means I'm yours enough to be laughed at, loved at, and never let go of.",
        ],
    },
    {
        "title": "We Never Gave Up",
        "subtitle": "the difficulties, and the choosing anyway",
        "eyebrow": "chapter eight",
        "paras": [
            "We didn't get the easy version of this. There were situations that could have quietly ended us, days that tested whether this was real or just convenient.",
            "But every single time, we chose each other again. Not because it was simple, but because walking away was never actually an option we considered — just one we survived not taking.",
            "We listened when it would have been easier to argue. We stayed when it would have been easier to leave. That, more than anything, is our favorite memory: not one moment, but the whole habit of not giving up.",
        ],
    },
    {
        "title": "Your Smile",
        "subtitle": "a short one, because it deserves its own page",
        "eyebrow": "chapter nine",
        "paras": [
            "Your smile doesn't ask for attention, which is exactly why it gets all of mine.",
            "It shows up crooked sometimes, half-hidden sometimes, and full and unguarded on the good days — and I've learned to read your whole mood just from the shape of it.",
            "If I ever build anything good in this life, I hope it's the kind of good that keeps that smile around.",
        ],
    },
    {
        "title": "Your Eyes",
        "subtitle": "where I stopped looking for anything else",
        "eyebrow": "chapter ten",
        "paras": [
            "I've never been good at poetry about eyes, so I'll just tell you the truth: yours are the first thing I look for, and the last thing I think about.",
            "They give you away — tired, amused, annoyed at me, softening anyway. I've learned your whole language just by watching them.",
            "I could describe the color. I'd rather describe what they do to me. That's the part that actually matters.",
        ],
    },
    {
        "title": "Your Hair",
        "subtitle": "small things I notice",
        "eyebrow": "chapter eleven",
        "paras": [
            "The way you push your hair back without thinking about it has, somehow, become one of my favorite things to watch.",
            "It's a small, unimportant gesture, and I've built an entire soft spot around it anyway.",
            "That's the thing about loving someone properly — even the details that were never meant to be noticed become the ones you remember best.",
        ],
    },
    {
        "title": "The Way You Talk",
        "subtitle": "your voice, your rambles, your rants",
        "eyebrow": "chapter twelve",
        "paras": [
            "You talk with your whole self — hands, tone, tangents that somehow circle back to the point right when I think you've lost it.",
            "I love listening to you explain something you care about. I love it even more when you're annoyed and trying to stay calm about it and failing a little, on purpose, for effect.",
            "I could listen to you talk about nothing for hours. I have. I'd do it again tomorrow.",
        ],
    },
    {
        "title": "Your Hands",
        "subtitle": "the ones that hold on",
        "eyebrow": "chapter thirteen",
        "paras": [
            "There's a specific kind of calm that shows up when your hand finds mine — like a sentence finally landing on the right word.",
            "Your hands write the notes that started this whole thing. They also hold on tightly on the days that are harder than the rest.",
            "I notice them more than I probably admit. They're doing quiet, important work, all the time.",
        ],
    },
    {
        "title": "Every Little Thing",
        "subtitle": "a list poem, because some things deserve a list",
        "eyebrow": "chapter fourteen",
        "paras": [
            "Your nose when you scrunch it up mid-argument. Your ears when they turn red before you admit I'm right. The curve of your neck when you tilt your head, half-listening, half-teasing.",
            "Your eyebrows doing all the talking your mouth hasn't caught up to yet. Your mouth, when it finally does.",
            "The quiet grace in how you walk into a room like you own it a little, and how you dance like you don't care that you don't — which somehow makes it better.",
            "And the two words that are only ours — my chocolate, my dessert — secrets I'm not writing the meaning of anywhere, because some things are just for us.",
            "None of it is the reason I love you. All of it is proof that I do.",
        ],
    },
    {
        "title": "Your Personality",
        "subtitle": "the actual reason",
        "eyebrow": "chapter fifteen",
        "paras": [
            "You're stubborn in the exact way that makes you loyal. You argue like you mean it and forgive like you mean that too.",
            "You notice when I'm quiet for the wrong reasons. You remember things I mentioned once, weeks ago, like they mattered — because to you, they did.",
            "I've met a lot of people who were easy to like. You're the first one who was worth learning properly. Every layer of you has been worth the time.",
        ],
    },
    {
        "title": "A Letter for the Hard Days",
        "subtitle": "for whenever you need to read this",
        "eyebrow": "chapter sixteen",
        "paras": [
            "Prashu,",
            "If you're reading this on a day that's heavy — I need you to know that none of what we've built is fragile. We've already survived harder days than today.",
            "You don't have to be okay for me to stay. You don't have to explain the bad mood or apologize for needing space or silence. I'm not going anywhere, and I'm not keeping score.",
            "Whatever it is, tell me or don't. Either way, come find me when you're ready. I'll still be here, exactly where you left me.",
        ],
        "letter": True,
        "sign": "— Sammu",
    },
    {
        "title": "A Letter for No Reason At All",
        "subtitle": "just because",
        "eyebrow": "chapter seventeen",
        "paras": [
            "Prashu,",
            "This one isn't for a hard day or an anniversary. I just felt like telling you, on an ordinary Tuesday kind of day, that I love you a lottttttt — more than I know how to type properly, apparently.",
            "Some days don't need a reason. I just wanted you to have proof, in writing, that you were thought about on a day that didn't ask for it.",
            "That's all. Go back to whatever you were doing. I just needed you to know.",
        ],
        "letter": True,
        "sign": "— Sammu",
    },
    {
        "title": "Punti & Bauni",
        "subtitle": "the ridiculous, wonderful in-between",
        "eyebrow": "chapter eighteen",
        "paras": [
            "Not every chapter of us needs to be serious. Half of what we are is nonsense — names invented for no reason, jokes that only make sense to two people, arguments about nothing that end in laughing.",
            "Punti. Bauni. Words that mean nothing outside this relationship and everything inside it.",
            "I think that's my favorite kind of love, honestly — the kind that has room for being ridiculous, because it's already sure of itself underneath.",
        ],
    },
    {
        "title": "What Forever Looks Like",
        "subtitle": "the future we talk about",
        "eyebrow": "chapter nineteen",
        "paras": [
            "We don't need a complicated plan. Just you and me, on the other side of all of this, building an ordinary, happy life together.",
            "A place that's ours. Mornings that aren't rushed. Arguments that still end in someone reaching for the other's hand first.",
            "I don't know every detail of what's ahead. I just know I want all of it to have you in it — Prashi, Baby, Punti, Bauni, Prashu, all of you, for all of it.",
        ],
    },
    {
        "title": "The Last Note",
        "subtitle": "closing this book, not this story",
        "eyebrow": "chapter twenty",
        "paras": [
            "Prashu,",
            "We started with a note asking for help. I hope this whole book counts as me finally paying that favor back — a hundred pages of proof that I noticed you, that I chose you, that I'm not planning on stopping.",
            "Every difficulty we've survived, every name I call you, every ordinary Tuesday and every June 6th to come — I want it all, with you, kutta and all.",
            "This is the last page of the book. It's not the last note. There's always going to be another one.",
        ],
        "letter": True,
        "sign": "— always, Sammu",
    },
]

# ---------------------------------------------------------------------------
# Templates
# ---------------------------------------------------------------------------

PAGE_TMPL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — For Prashu</title>
<link rel="stylesheet" href="../assets/style.css">
</head>
<body>
<header class="topbar">
  <a class="home-link" href="../index.html"><span class="notes-mark"></span> For Prashu</a>
  <a href="../contents.html">Contents</a>
</header>
<main class="page">
  <span class="tab">chapter {num} of {total}</span>
  <div class="chapter-head">
    <span class="eyebrow">{eyebrow}</span>
    <h1>{title}</h1>
    <div class="subtitle">{subtitle}</div>
    <hr class="rule">
  </div>
  <article class="prose">
    {body}
  </article>
  <div class="pagefoot">
    <span>{prev_link}</span>
    <a class="mid" href="../contents.html">contents</a>
    <span>{next_link}</span>
  </div>
</main>
</body>
</html>
"""

def make_body(ch):
    cls = "stanza" if not ch.get("letter") else ""
    parts = [f'<p class="{cls}">{p}</p>' if cls else f"<p>{p}</p>" for p in ch["paras"]]
    if ch.get("letter"):
        parts.append(f'<p class="signoff">{ch["sign"]}</p>')
    return "\n    ".join(parts)

def slug(n):
    return f"{n:02d}"

total = len(CHAPTERS)
for i, ch in enumerate(CHAPTERS, start=1):
    prev_link = f'<a href="{slug(i-1)}.html">&larr; previous</a>' if i > 1 else '<span></span>'
    next_link = f'<a href="{slug(i+1)}.html">next &rarr;</a>' if i < total else '<a href="../closing.html">closing page &rarr;</a>'
    html = PAGE_TMPL.format(
        title=ch["title"],
        num=i,
        total=total,
        eyebrow=ch["eyebrow"],
        subtitle=ch["subtitle"],
        body=make_body(ch),
        prev_link=prev_link,
        next_link=next_link,
    )
    with open(os.path.join(CH_DIR, f"{slug(i)}.html"), "w", encoding="utf-8") as f:
        f.write(html)

# ---------------------------------------------------------------------------
# contents.html
# ---------------------------------------------------------------------------

toc_items = []
for i, ch in enumerate(CHAPTERS, start=1):
    toc_items.append(
        f'<li><a href="chapters/{slug(i)}.html"><span class="num">{i:02d}</span>'
        f'<span class="ttl">{ch["title"]}</span><span class="sub">{ch["subtitle"]}</span></a></li>'
    )

CONTENTS_TMPL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Contents — For Prashu</title>
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<header class="topbar">
  <a class="home-link" href="index.html"><span class="notes-mark"></span> For Prashu</a>
  <a href="chapters/01.html">Start reading &rarr;</a>
</header>
<main class="page">
  <div class="chapter-head">
    <span class="eyebrow">a book of notes, poems &amp; letters</span>
    <h1>Contents</h1>
    <div class="subtitle">twenty small chapters, one whole heart</div>
    <hr class="rule">
  </div>
  <ul class="toc-list">
    {items}
  </ul>
</main>
</body>
</html>
"""

with open(os.path.join(ROOT, "contents.html"), "w", encoding="utf-8") as f:
    f.write(CONTENTS_TMPL.format(items="\n    ".join(toc_items)))

# ---------------------------------------------------------------------------
# closing.html (final page after chapter 20)
# ---------------------------------------------------------------------------

CLOSING_TMPL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>The End — For Prashu</title>
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<header class="topbar">
  <a class="home-link" href="index.html"><span class="notes-mark"></span> For Prashu</a>
  <a href="contents.html">Contents</a>
</header>
<main class="cover" style="min-height:70vh;">
  <div class="marks"><div class="note a"></div><div class="note b"></div><span class="heart">&#10084;</span></div>
  <span class="eyebrow">the notebook closes here</span>
  <h1 style="font-size:clamp(2.2rem,6vw,3.4rem);">until the next note</h1>
  <p class="tagline">June 6, 2025, to every ordinary day after it &mdash; still choosing you, still not giving up.</p>
  <p class="byline">Sammu &amp; Prashu</p>
  <a class="cta" href="contents.html">Read it again</a>
</main>
</body>
</html>
"""

with open(os.path.join(ROOT, "closing.html"), "w", encoding="utf-8") as f:
    f.write(CLOSING_TMPL)

print(f"Generated {total} chapters + contents.html + closing.html")
