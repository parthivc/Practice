#include <bits/stdc++.h>
using namespace std;

long long getSum(long long BITree[], long long index) 
{ 
    long long sum = 0; // Initialize result 
  
    // Traverse ancestors of BITree[index] 
    while (index > 0) 
    { 
        // Add current element of BITree to sum 
        sum += BITree[index]; 
  
        // Move index to parent node in getSum View 
        index -= index & (-index); 
    } 
    return sum; 
} 

void updateBIT(long long BITree[], long long n, long long index, long long val) 
{ 
    // Traverse all ancestors and add 'val' 
    while (index <= n) 
    { 
       // Add 'val' to current node of BI Tree 
       BITree[index] += val; 
  
       // Update index to that of parent in update View 
       index += index & (-index); 
    } 
} 

void convert(vector<long long> & arr, long long n) 
{ 
    // Create a copy of arrp[] in temp and sort the temp array 
    // in increasing order 
    long long temp[n]; 
    for (long long i=0; i<n; i++) 
        temp[i] = arr[i]; 
    sort(temp, temp+n); 
  
    // Traverse all array elements 
    for (long long i=0; i<n; i++) 
    { 
        // lower_bound() Returns polong longer to the first element 
        // greater than or equal to arr[i] 
        arr[i] = lower_bound(temp, temp+n, arr[i]) - temp + 1; 
    } 
} 

long long getInvCount(vector<long long> & arr, long long & n) 
{ 
    // Convert arr[] to an array with values from 1 to n and 
    // relative order of smaller and greater elements remains 
    // same.  For example, {7, -90, 100, 1} is converted to 
    //  {3, 1, 4 ,2 } 
    convert(arr, n); 
  
    // Create and initialize smaller and greater arrays 
    long long greater1[n], smaller1[n]; 
    for (long long i=0; i<n; i++) 
        greater1[i] = smaller1[i] = 0; 
  
    // Create and initialize an array to store Binary 
    // Indexed Tree 
    long long BIT[n+1]; 
    for (long long i=1; i<=n; i++) 
        BIT[i]=0; 
  
    for(long long i=n-1; i>=0; i--) 
    { 
        smaller1[i] = getSum(BIT, arr[i]-1); 
        updateBIT(BIT, n, arr[i], 1); 
    } 
  
    // Reset BIT 
    for (long long i=1; i<=n; i++) 
        BIT[i] = 0; 
  
    // Count greater elements 
    for (long long i=0; i<n; i++) 
    { 
        greater1[i] = i - getSum(BIT,arr[i]); 
        updateBIT(BIT, n, arr[i], 1); 
    } 
  
    // Compute Inversion count using smaller[] and 
    // greater[].  
    long long invcount = 0; 
    for (long long i=0; i<n; i++) 
        invcount += smaller1[i]*greater1[i]; 
  
    return invcount; 
} 

int main(){
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	long long ret = 0;
	long long n;
	cin >> n;
	vector<long long> v(n);
	for(long long i =0; i < n; i++)
		cin >> v[i];
	cout << getInvCount(v, n) << endl;
	return 0;
}