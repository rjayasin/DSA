# create a mapping of target -> (pair) (index1, index2)
# loop once more over list of nums to find target
import random

def three_sum(nums, target):
    targets = {}
    indexes = set()
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j: continue
            if (i, j) in indexes or (j, i) in indexes: continue
            indexes.add((i, j))
            s = target - (nums[i] + nums[j])
            if s in targets:
                targets[s].append(((nums[i], nums[j]), 
                                    {i, j}))
            else:
                targets[s] = [((nums[i], nums[j]),
                                {i, j})]

    results = set()
    for n in range(len(nums)):
        if nums[n] in targets:
            cand = targets[nums[n]]
            for poss in cand:
                if n not in poss[1]:
                    results.add(poss[0] + (nums[n],))
    return results


if __name__ == '__main__':
    nums = [random.randrange(-3, 5) for _ in range(5)]
    target = random.randrange(-1, 8)
    x = three_sum(nums, target)
    print(nums, target)
    print(x)
