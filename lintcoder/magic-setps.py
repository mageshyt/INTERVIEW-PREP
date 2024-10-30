"""
In a mystical land, there exists an enchanted staircase with an
infinite number of steps, starting from the bottom step numbered
0. A wizard named Merlin has an integer spell power, initially set
to 0. Merlin starts his journey on step 1 and wants to reach step
K using any number of magical operations. If he is on step i, in one
operation he can:
Cast a spell to move down to step i-1. This spell cannot
be cast consecutively or on step 0.
Use a magic spell to teleport to step i+2^(spell power).
After this spell, his spell power increases by 1.
Your task is to calculate the total number of ways Merlin can reach
step K.
Note that it is possible for Merlin to reach step K and then perform
additional operations to return to step K again.

Testcase Input
0

Testcase Output
The 2 possible ways of reaching step 0 are:
Way 1: Merlin starts at step 1 and moves down 1 step to reach step
Way 2: Merlin starts at step 1, moves down 1 step to reach step 0,
teleports up 2^0=1 step to reach step 1, then moves down 1 step
to reach step 0. (Now his spell power became 1, so he can't
perform "way 2" consecutively).

"""
def ways_to_reach_k(k: int) -> int:
    if k == 0:
        return 2

    dp = {}


    def dfs(step, spell_power, prev_spell):
        # print(f"[{step,spell_power,prev_spell}]")
        if step == k:
            return 1

        if step > k and prev_spell == "down":
            return 0


        if (step, spell_power, prev_spell) in dp:
            # print("RETURNING ANS ",dp[(step, spell_power, prev_spell)])
            return dp[(step, spell_power, prev_spell)]


        ways = 0

        if  prev_spell != "down":
            ways += dfs(step - 1, spell_power, "down")

        else:
            ways += dfs(step+2**spell_power, spell_power+1, "teleport")
        dp[(step, spell_power, prev_spell)] = ways
        # print("WAYS ",ways)
        return ways

    # Try two spell from k-1 and k+2^spell_power
    total_ways = dfs(1, 0, "teleport") + dfs(1, 0, "down")
        # print(dp)

    return total_ways

print(ways_to_reach_k(1))  # 4
print(ways_to_reach_k(4))  # 4 /