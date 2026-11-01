# Last Bronx (Sega Saturn, Sega AM3, 1997) reverse-engineering notes and symbols

Hand-named function map, naming prompt and tools for **Last Bronx** (MK-81078, Europe): the boot loader `BRONX.EXE` (SH-2, 0x06009800) and the three game programs `LB.EXE`, `LB2.EXE`, `LBMP.EXE` (all loaded at 0x0600d300; one in memory at a time). LB2/LBMP share most code with LB.EXE and got its names by byte match first.
Current state (after round 1 naming + one review round on the main program):

| Program | Functions | Named | Provisional |
|---|---|---|---|
| LB | 1,168 | 1,168 | 36 |
| LB2 | 1,096 | 1,096 | 103 |
| LBMP | 279 | 279 | 116 |
| BRONX | 65 | 65 | 14 |

0 `FUN_` placeholders left.

- Round 1 (11-01): every function Ghidra found (SH-2 `4f22`/`2fe6` prologue seeding + `CreateAt.java`) named from its decompile and strings in ~150-function slices by Sonnet agents; unsure names carry `provisional` in the comment.
- Review round 1 (11-01): the main program's provisional names re-read with callers/callees (`ghidra/review/all_*_rv.txt`: `<prog> 0x<addr> <old> CONFIRM/RENAME/UNSURE <new> <reason>`).
- Overlays: names copied from already-named programs by masked byte hashes (`tools/xmatch.py`: SH-2 literal-pool words that look like pointers are masked, a name is copied only on a unique match), the rest named like round 1.

Subsystem prefixes (most common first): vdp2_, stm_ (streams), sgl_ (Sega Graphics Library), aud_/snd_/scsp_, pad_/input_, ai_, fighter_, math_, menu_, cam_, cd_, charsel_, match_, hit_, anim_, save_, gfx_, sys_, fsm_.

Same method as [deadoralive-decomp](https://github.com/indieindie7/deadoralive-decomp). Non-commercial, done for study and preservation.

**No game data is included**: no disc image, no executables, no overlays, no decompiled C, no game text,
no Ghidra database. You need your own copy of the game to use any of this.

## What is here

| Path | Content |
|---|---|
| `NOTES.md` | disc layout, load bases and how they were found, pipeline, log |
| `ghidra/hand_<prog>.txt` | hand names: `0x<addr> func <name> hand <comment>` (apply with `ghidra/scripts/ApplyNames.java`, hand mode) |
| `ghidra/funcinfo_<prog>.tsv` | per-function export: `F` address name source size, `C` callees (string rows removed) |
| `ghidra/naming/` | the naming prompt |
| `ghidra/review/` | review verdict lines |
| `ghidra/scripts/` | `FindSh2FunctionsMem.java` (prologue seeding), `CreateAt.java`, `ApplyNames.java`, `ExportFuncInfo.java`, `CsDumpAll.java` / `DumpDecomp.java` (decompile dump), `DataRefs.java`, `DeleteFunctions.java` |
| `tools/` | `slice.py` (naming slices), `pubfuncinfo.py`, `xmatch.py` |

## Licence

Notes, names and tools: MIT (see `LICENSE`). Last Bronx belongs to its rights holders; nothing from the
game is distributed here.
