# @param {Integer[]} nums
# @return {String}
def triangle_type(nums)
    nums = nums.sort
    if nums.length < 3 || (nums[0] + nums[1] <= nums[2])
        return "none"
    end
    uni = nums.to_set
    if uni.length == 3
        return "scalene"
    elsif uni.length == 2
        return "isosceles"
    else
        return "equilateral"
    end
end