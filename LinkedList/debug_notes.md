# Debug Notes - Reverse Linked List II

## ❌ Initial Mistakes:
- Tried to apply reverse logic without handling the connections before/after `left` and `right`.
- Misunderstood how `curr` moves and how to reconnect reversed portion.
- Confused about how many iterations needed: off-by-one errors in loop range.
- Tried to link `prev.next = prev_sub` while `prev_sub` was still None.

## 💡 Final Understanding:
- Used a dummy node to simplify edge cases and maintain 0-indexing.
- Stored `prev` as the node before `left`, and `curr` as start of sublist.
- Tracked `tail = curr` (start of reverse) to reconnect the end.
- Reversed nodes in-place, same as Leetcode 206.
- After reversal:
    - `prev.next` connects to new head of reversed part.
    - `tail.next` connects to node after `right`.

## 🔁 Loop:
- `range(right - left + 1)` gives exact number of nodes to reverse.
- `curr` ends up pointing to `right+1` node after loop.

## ✅ Tips:
- When reversing in a section, always track:
    - Node before start (`prev`)
    - Node at start (`curr`)
    - Node at end (`curr` after loop)
- Dummy node avoids special-case handling at head.

## 🔍 Reference:
- This is a localized application of the full reverse problem (Leetcode 206).
