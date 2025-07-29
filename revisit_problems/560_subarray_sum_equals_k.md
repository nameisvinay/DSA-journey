
---

## 🔑 Subarray Sum Equals K – Simple Summary

* Maintain a running sum called `curr_sum`.
* Use a hashmap to store how many times each `curr_sum` has appeared.
* If `curr_sum - k` exists in the map, it means a subarray with sum `k` ends at the current index.
* Add the frequency of `curr_sum - k` to the answer count.
* Always update the hashmap with the current `curr_sum`.
* Do **not** store or update `curr_sum - k` — just check and use its frequency.

---
