def hanoi_solver(disks):
    A = list(range(disks, 0, -1))
    B = []
    C = []
    hanoi = [f'{A} {B} {C}']
    def move(disks, source, auxiliary, target):
        if disks == 1:
            target.append(source.pop())
            hanoi.append(f'{A} {B} {C}')
            return
        move(disks - 1, source, target, auxiliary)
        target.append(source.pop())
        hanoi.append(f"{A} {B} {C}")
        move(disks - 1, auxiliary, source, target)
    move(disks, A, B, C)
    return "\n".join(hanoi)

print(hanoi_solver(3))