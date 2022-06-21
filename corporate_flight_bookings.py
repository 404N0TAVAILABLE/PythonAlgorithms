# leetcode solution

class Solution:
  def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
    ans = [0] * n


    for booking in bookings:
        ans[booking[0] - 1] += booking[2]
        if booking[1] < n:
            ans[booking[1]] -= booking[2]

    for i in range(1, n):
        print(f'i is : {i}')                
        ans[i] += ans[i - 1]

    return ans


if __name__ == '__main__':

    n = 5
#    n = 2
    bookings = [[1,2,10],[2,3,20],[2,5,25]]
#    bookings = [[1,2,10],[2,2,15]]

    objSolution = Solution()

    print(objSolution.corpFlightBookings(bookings, n))
