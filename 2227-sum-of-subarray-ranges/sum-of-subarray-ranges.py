class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:

        # answer = 0

        # for i in range(0, len(nums)):
        #     temp = 0
        #     maxx = nums[i]
        #     minn = nums[i]
        #     for j in range (i, len(nums)):
        #         maxx = max ( maxx, nums[j])
        #         minn = min (minn, nums[j])
        #         temp = maxx - minn
        #         answer = answer + temp
        # return answer

        minSum = 0
        maxSum = 0

        stack = []
        pse = []
        nse = []


        for i in range(0, len(nums)):
            if len(stack) == 0:
                stack.append(i)
                pse.append(-1)

            else:

                if nums[stack[-1]] < nums[i]:
                    pse.append(stack[-1])
                    stack.append(i)

                else:

                    while len(stack) > 0 and nums[stack[-1]] >= nums[i]:
                        stack.pop()

                    if len(stack) > 0:
                        pse.append(stack[-1])
                    else:
                        pse.append(-1)

                    stack.append(i)

        # print(pse)

        stack.clear()

        for i in range(len(nums)-1, -1, -1):

            if len(stack) == 0:
                stack.append(i)
                nse.append(len(nums))

            else:

                if nums[stack[-1]] <= nums[i]:
                    nse.append(stack[-1])
                    stack.append(i)

                else:

                    while len(stack) > 0 and nums[stack[-1]] > nums[i]:
                        stack.pop()

                    if len(stack) > 0:
                        nse.append(stack[-1])
                    else:
                        nse.append(len(nums))

                    stack.append(i)

        nse = nse[::-1]

        # print(nse)

        for i in range(len(nums)):
            left = i - pse[i]
            right = nse[i] - i

            minSum += left * right * nums[i]

        # print(minSum)

        stack.clear()
        pse.clear()
        nse.clear()



        for i in range(0, len(nums)):

            if len(stack) == 0:
                stack.append(i)
                pse.append(-1)

            else:

                if nums[stack[-1]] > nums[i]:
                    pse.append(stack[-1])
                    stack.append(i)

                else:

                    while len(stack) > 0 and nums[stack[-1]] <= nums[i]:
                        stack.pop()

                    if len(stack) > 0:
                        pse.append(stack[-1])
                    else:
                        pse.append(-1)

                    stack.append(i)

        # print(pse)

        stack.clear()

        for i in range(len(nums)-1, -1, -1):

            if len(stack) == 0:
                stack.append(i)
                nse.append(len(nums))

            else:

                if nums[stack[-1]] >= nums[i]:
                    nse.append(stack[-1])
                    stack.append(i)

                else:

                    while len(stack) > 0 and nums[stack[-1]] < nums[i]:
                        stack.pop()

                    if len(stack) > 0:
                        nse.append(stack[-1])
                    else:
                        nse.append(len(nums))

                    stack.append(i)

        nse = nse[::-1]

        # print(nse)

        for i in range(len(nums)):
            left = i - pse[i]
            right = nse[i] - i

            maxSum += left * right * nums[i]

        # print(maxSum)

        return maxSum - minSum