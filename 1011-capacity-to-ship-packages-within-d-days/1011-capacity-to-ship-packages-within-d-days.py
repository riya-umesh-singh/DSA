class Solution:
    def shipWithinDays(self, weights, days):
         l = max(weights)
         h = sum(weights)
         while l<=h:
          mid = (l + h)//2
          curr_w = 0 
          use_day = 1
          for weig in weights:

            if curr_w + weig <= mid:
                curr_w += weig
            else:
                use_day += 1
                curr_w = weig

          if use_day <= days:
                h = mid - 1
          else:
                l = mid + 1

         return l
               






























            