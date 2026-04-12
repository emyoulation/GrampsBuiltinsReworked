Now let me fetch the raw file for cleaner reading: I have enough from the rendered view. 
Let me also look at the BatchTool base class and the existing Ok Cancel Dialog patterns for guidance: I have a thorough understanding of the codebase from the source. 
Let me now build the enhanced `eventnames.py`: There's a typo in the `rb_box` construction line — let me fix it:
Now let's do a quick syntax check: Clean. 
Let me view the final file to make one last review pass: Looks solid. 
Let me present it: Here's a summary of every change made and the reasoning behind each decision.

---

## What changed and why

### New class: `EventNamesDialog`

This replaces the role previously played by the bare "Undo history warning" that `BatchTool.__init__` fires automatically. By wiring the dialog into `_show_dialog_and_run()` — which is called **after** `BatchTool.__init__` completes but before any database work begins — the user sees a purposeful, tool-specific dialog instead of a generic alarm.

The dialog contains:

| UI element | Purpose |
|---|---|
| Information icon + explanation label | Explains what the tool does so accidental triggering is obvious |
| **Add** radio (default, pre-selected) | Preserves original behaviour — fills blank descriptions |
| **Remove** radio | Reverses a prior run — the new reciprocal action |
| Dynamic hint label (`dim-label`) | Updates live to explain exactly what each mode will and won't touch |
| **Stop** button (`CANCEL`) | Safe exit with no changes, no undo history pollution |
| **Proceed with the Tool** button (`suggested-action`) | GTK accent styling makes the intentional path clear |

### New mode: `MODE_REMOVE` / `_run_remove()`

The remove pass re-derives the exact string that `person_event_name` / `family_event_name` *would* produce for each event's current primary person or family, then compares it to the stored description. Only an exact match triggers a clear. This means:

- Descriptions the user wrote themselves (even if they happen to contain the event type name) are safe unless they match the template character-for-character.
- The same `EVENT_PERSON_STR` / `EVENT_FAMILY_STR` module-level format strings are reused in `_matches_person_pattern` and `_matches_family_pattern`, so any future localisation change automatically keeps Add and Remove in sync.

### `EventNames.__init__` restructure

`_show_dialog_and_run()` captures the parent window once, builds the dialog, reads the chosen mode, destroys the dialog, and dispatches to `_run_add` or `_run_remove`. If the user clicks **Stop**, the method returns immediately — the undo stack is never touched.

### Commit message (for your reference)

```
Add pre-run dialog with Add/Remove modes to Extract Event Descriptions tool.

The existing undo-history warning dialog provided no useful context and
was too easy to dismiss accidentally when the tool was not intended to
be run.  This change replaces it with a purpose-built EventNamesDialog
offering two clearly labelled radio options:

  • Add descriptions to events with blank descriptions (original behaviour,
    selected by default).
  • Remove descriptions that match the auto-generated pattern, reversing a
    previous run without touching manually-authored descriptions.

A Stop button exits cleanly before any database transaction is opened.

Generated-by: Claude Sonnet 4.6, Anthropic (claude-sonnet-4-6)
Prompt: "develop a new dialog to supplant the Undo history warning dialog
with Stop and Proceed buttons that provides a reciprocal option to clear
any description that matches what the Tool might have added previously"
```
