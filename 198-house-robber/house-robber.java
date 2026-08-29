class Solution {
    public int rob(int[] nums) {
        
        int l = nums.length;
        if(l==0){
            return 0;
        }
        if(l==1){
            return nums[0];
        }
        int[] arr = new int[l];
        arr[0] = nums[0];
        arr[1] = Math.max(nums[0],nums[1]);
        for(int i=2;i<=l-1;i++){
            arr[i] = Math.max(arr[i-1],nums[i]+arr[i-2]);
        }
        return arr[l-1];
    }
}