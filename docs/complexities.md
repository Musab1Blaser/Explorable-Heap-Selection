| Algorithm                               | Time                                      | Space              |
| --------------------------------------- | ----------------------------------------- | ------------------ |
| Original (Deterministic)                | $n \cdot \exp(O(\sqrt{\log n}))$          | $O(\log^{2.5}(n))$ |
| Original (Randomized)                   | $n \cdot \exp(O(\sqrt{\log n}))$          | $O(\sqrt{\log n})$ |
| Proposed (Randomized)                   | $O(n \log^3 (n))$                         | $O(\log n)$        |
| Theoretical Limit (on time given space) | $\Omega(\frac{n \log(n)}{\log(\log (n)})$ | $O(\log n)$        |
