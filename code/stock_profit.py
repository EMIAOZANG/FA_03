'''
stpb
'''

class StockProfit:

	def max_min_maxsubarray(self,A,low,high):
	    '''
	    A: input array
	    low, high: cursor boundaries
	    
	    returns : a list (alpha,beta,i,j,max_subarray)
	    '''
	    if low >= high:
	        return (low,high,low,high,0)
	    mid = (high+low)/2
	#    print 'low: {}, high: {}, mid: {}'.format(low, high, mid)
	    alpha_left, beta_left, i_left, j_left, max_sub_left = self.max_min_maxsubarray(A,low,mid)
	    alpha_right, beta_right, i_right, j_right, max_sub_right = self.max_min_maxsubarray(A,mid+1,high)
	    
	    #computing new params
	    if A[alpha_left] <= A[alpha_right]:
	        alpha = alpha_left
	    else:
	        alpha = alpha_right
	    if A[beta_right] >= A[beta_left]:
	        beta = beta_right
	    else:
	        beta = beta_left
	
	    if alpha <= beta:
	        i = alpha
	        j = beta
	        max_sub = A[j]-A[i]
	    else:
	        #if index(max) > index(min), then the max_sub is the maximum of the two subarrays
	        max_sub = max(max_sub_left,max_sub_right)
	        if A[j_left]-A[i_left] >= A[j_right]-A[i_right]:
	            i = i_left
	            j = j_left
	        else:
	            i = i_right
	            j = j_right
	    return (alpha, beta, i, j, max_sub)
    
    #solve the problem in linear time
	def max_profit(A):
	    if len(A) == 0:
	        return (0,0,0)
	    min_val = A[0]
	    min_index = 0
	    max_index = 0
	    max_profit = 0
	    for i in range(0,len(A)):
	        if A[i] < min_val:
	            min_val = A[i]
	            min_index = i 
	        if A[i]-min_val >= max_profit:
	            max_profit = A[i]-min_val 
	            max_index = i
	    return min_index, max_index, max_profit 



#def main():
#    ll = [6,4,1,2,3,9,7,5]
#    print max_min_maxsubarray(ll,0,7)

#if __name__ == "__main__":
#    main()

 

