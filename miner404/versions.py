from .pipeline import Draft, StagePlan, Step

ACTIVE_PLAN = StagePlan(
    drafts=(
        Draft(start='plain', model='gpt-6.1-sol', effort='high'),
        Draft(start='proportions', model='gpt-6.1-sol', effort='high'),
        Draft(start='plain', model='gpt-6.1-sol', effort='high'),
        Draft(start='proportions', model='gpt-6.1-sol', effort='high'),
        Draft(start='plain', model='gpt-6.1-sol', effort='high'),
        Draft(start='proportions', model='gpt-6.1-sol', effort='high'),
    ),
    steps=(
        Step(rewrites=(('gpt-6.1-sol', 'xhigh'),), focus=('materials', 'shape'), fallback=('gpt-6.1-sol', 'high'), info=('gate',)),
        Step(rewrites=(('gpt-6-astra', 'high'),), focus=('materials', 'shape'), fallback=('gpt-6.1-sol', 'xhigh'), info=('gate',)),
        Step(rewrites=(('gpt-6.1-sol', 'xhigh'),), fallback=('gpt-6.1-sol', 'high'), info=('gate',)),
        Step(rewrites=(('gpt-6.1-sol', 'xhigh'),), fallback=('gpt-6.1-sol', 'high'), info=('gate',)),
        Step(rewrites=(('gpt-6-astra', 'high'),), fallback=('gpt-6.1-sol', 'xhigh'), info=('gate',)),
        Step(rewrites=(('gpt-6.1-sol', 'max'),), fallback=('gpt-6.1-sol', 'xhigh'), info=('gate',), nudge=' Before anything else, compare the reference photo with the current model for small visible details that the model leaves out or simplifies, and add or sharpen the most visible of them, keeping the overall shape, proportions, pose and colours as they are.'),
        Step(rewrites=(('gpt-6-astra', 'high'),), fallback=('gpt-6.1-sol', 'xhigh'), info=('gate',), nudge=' Before anything else, compare the reference photo with the current model for small visible details that the model leaves out or simplifies, and add or sharpen the most visible of them, keeping the overall shape, proportions, pose and colours as they are.'),
        Step(rewrites=(('gpt-6.1-sol', 'xhigh'),), fallback=('gpt-6.1-sol', 'high'), info=('gate',), nudge=' Before anything else, compare the reference photo with the current model for small visible details that the model leaves out or simplifies, and add or sharpen the most visible of them, keeping the overall shape, proportions, pose and colours as they are.'),
        Step(rewrites=(('gpt-6.1-sol', 'xhigh'),), fallback=('gpt-6.1-sol', 'high'), info=('gate',), nudge=' Before anything else, compare the reference photo with the current model for small visible details that the model leaves out or simplifies, and add or sharpen the most visible of them, keeping the overall shape, proportions, pose and colours as they are.'),
        Step(rewrites=(('gpt-6.1-sol', 'xhigh'),), fallback=('gpt-6.1-sol', 'high'), info=('gate',), nudge=' Before anything else, compare the reference photo with the current model for small visible details that the model leaves out or simplifies, and add or sharpen the most visible of them, keeping the overall shape, proportions, pose and colours as they are.'),
        Step(rewrites=(('gpt-6.1-sol', 'xhigh'),), fallback=('gpt-6.1-sol', 'high'), info=('gate',), nudge=' Before anything else, compare the reference photo with the current model for small visible details that the model leaves out or simplifies, and add or sharpen the most visible of them, keeping the overall shape, proportions, pose and colours as they are.'),
        Step(rewrites=(('gpt-6.1-sol', 'xhigh'),), fallback=('gpt-6.1-sol', 'high'), patch=True, info=('gate',), nudge=' Before anything else, compare the reference photo with the current model for small visible details that the model leaves out or simplifies, and add or sharpen the most visible of them, keeping the overall shape, proportions, pose and colours as they are.'),
        Step(rewrites=(('gpt-6.1-sol', 'xhigh'),), fallback=('gpt-6.1-sol', 'high'), patch=True, info=('gate',), nudge=' Before anything else, compare the reference photo with the current model for small visible details that the model leaves out or simplifies, and add or sharpen the most visible of them, keeping the overall shape, proportions, pose and colours as they are.'),
    ),
    draft_keep=1,
    fill=0.999,
    render_cap=76,
    keep_dark=True,
)
