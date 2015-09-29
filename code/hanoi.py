'''
hanoi tower problem
'''

class Hanoi:
    def cyclic_hanoi(n_disks, src, via, dst):
        '''
        Let a_n be the number of moves needed to move n disks forward by 1 steps, b_n be the number of moves to move n disks forward 2 steps
        then we have a_n = 2b_(n-1) + 1
        since if we want to move 1,...,n from A to C
        we need to move 1,...,n-1 from A to B to C, then move n from A to B, then move 1,...,n-1 from C to B to A

        similarly, if we want to move 1,...,n from A to B, the moving sequence will be:
        1. move 1,...,n-1 from A to B to C
        2. move n from A to B
        3. move 1,...,n-1 from C to A
        4. move n from B to C
        5. move 1,...,n-1 from A to B to C
        therefore, b_n = 2b_(n-1) + a_(n-1) + 2 = 2b_(n-1) + 2b_(n-2) + 3
        We could solve this recurrence and get b_n = O((1+sqrt(3))^n)
        '''
        if n_disks == 1:
            print src, ' -> ', via
            print via, ' -> ', dst

