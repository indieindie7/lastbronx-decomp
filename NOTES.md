# Last Bronx (Saturn) decomp — NOTES
## Index
1. Source + layout  2. Pipeline  3. Log
## 1. Source + layout
- User 11-01: <own disc rip> (Europe, 24 tracks, disc 'Last Bronx (Europe)'). Unpacked: saturn/image (bin/cue), saturn/cd (isoextract.py 2352, Scorcher/tools).
- IP.BIN: SEGA SEGASATURN, MK-81078 V1.001, 1997-09-10, area E, 1st read addr 0x06009800 = BRONX.EXE.
- Main exe LB.EXE, load base 0x0600d300 (verified: call/pointer targets hit SH-2 prologues 4f22 best at this base).
- saturn/cd = 470 files, 105.7 MB (MAIN/ 451 fighter/stage/camera BIN, MOVIE/*.AVI are 0-byte in the rip). Boot file BRONX.EXE (15084 B, base 0x06009800, 59 fns, loader). Game exes all at 0x0600d300: LB.EXE 704736 B (imported, 949 prologues, code first), LB2.EXE 731552 B (data first, code from file+0x45a10, entry 0x06052e60, 889 prologues; likely variant/second mode), LBMP.EXE 145060 B (menu/mode, 165 prologues). Not imported yet: BRONX.EXE, LB2.EXE, LBMP.EXE (which one BRONX loads when is unresolved).
- Never push disc data. No public decomp checked.
## 2. Pipeline (copied from DeadOrAlive 10-27)
- ghidra/run.sh <abs log> <args> (project LB in ghidra/), ghidra/import.sh <file in bin/> <base> = import SH-2 + FindSh2FunctionsMem + CreateAt + ExportFuncInfo + CsDumpAll. Runs with HOGGATE=ok when hoggate blocks.
- tools/slice.py <decomp> ghidra/naming <P> -> ~150-fn naming slices. Prompt ghidra/scripts/prompt_LB.txt (from prompt_DOA.txt).
- Then naming (Sonnet agents -> naming/q_<n>.txt), hand_<exe>.txt, ApplyNames, export, provisional review, publish.
## 3. Log
- 11-01: import LB.EXE @0x0600d300 DONE: F=1168 functions (funcinfo_LB.tsv, decomp_LB.c). 8 slices ghidra/naming/LB_1..8.c. No names applied yet (all FUN_).
- 11-01: names merged (mergeapply.sh), ApplyNames + export done; counts above.
- 11-01: imported BRONX.EXE 0x06009800 F=65, LB2.EXE F=1096, LBMP.EXE F=279 (0x0600d300). tools/xmatch.py byte-matched LB names: LB2 601, LBMP 100 (hand_LB2/LBMP.txt).
- 11-01: review r1 (Sonnet, review/t_*_rv.txt -> all_*_rv.txt, backup hand_*.r0.txt) applied; 35 provisional left; FUN=0.
- 11-01: overlay names merged: LB2 1096 (321 prov), LBMP 279 (168), BRONX 65 (14); FUN=0.
- 11-01: LB review renames propagated to LB2/LBMP by name map (hand_LB.r0 -> hand_LB; backups hand_LB2/LBMP.r0.txt): LB2 219 updated, prov 103; LBMP 52 updated, prov 116; FUN=0.
