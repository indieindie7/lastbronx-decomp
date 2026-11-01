# xmatch.py <binA> <baseA> <funcinfoA> <handA> <binB> <baseB> <funcinfoB> <out hand B>: copy names A->B for
# functions whose bytes match (SH-2: 16-bit opcodes; 32-bit words that look like pointers into either image masked).
import sys, hashlib
bA, baseA, fA, hA, bB, baseB, fB, out = sys.argv[1:9]; baseA = int(baseA, 16); baseB = int(baseB, 16)
def funcs(f):
    r = []
    for l in open(f, encoding='utf-8', errors='replace'):
        p = l.split()
        if p[0] == 'F': r.append((int(p[1], 16), p[2], int(p[4])))
    return r
def key(d, base, a, n):
    b = bytearray(d[a - base:a - base + n])
    for i in range(0, len(b) - 3, 2):
        w = int.from_bytes(b[i:i+4], 'big')
        if 0x06000000 <= w < 0x06100000 or 0x00200000 <= w < 0x00300000: b[i:i+4] = b'PPPP'
    return hashlib.md5(bytes(b)).hexdigest() + str(n)
dA, dB = open(bA, 'rb').read(), open(bB, 'rb').read()
names = {}
for l in open(hA, encoding='utf-8', errors='replace'):
    p = l.split(None, 3)
    if len(p) >= 3 and p[1] == 'func': names[int(p[0], 16)] = l.split(None, 2)[2].rstrip('\n')
ka = {}
for a, nm, n in funcs(fA):
    if a in names and n > 8: ka.setdefault(key(dA, baseA, a, n), []).append(a)
used, w, m = set(), [], 0
for a, nm, n in funcs(fB):
    if n <= 8: continue
    c = ka.get(key(dB, baseB, a, n))
    if c and len(c) == 1:
        rest = names[c[0]]; nm2 = rest.split()[0]
        if nm2 in used: continue
        used.add(nm2); m += 1
        w.append('0x%08x func %s' % (a, rest))
open(out, 'w').write('\n'.join(w) + '\n')
print('matched', m, 'of', len(funcs(fB)))
