import * as ed from '@noble/ed25519';

var point1 = ed.ExtendedPoint.BASE.double();
var point2 = ed.ExtendedPoint.BASE.multiplyUnsafe(BigInt(2));

var n = BigInt(2);
var p = ed.ExtendedPoint.ZERO;
var d = ed.ExtendedPoint.BASE;
while (n > BigInt(0)) {
    if (n & BigInt(1))
        console.log("add");
        p = p.add(d);
    d = d.double();
    console.log("double");
    n >>= BigInt(1);
    console.log(n);
}
//var p2 = point1.double();
console.log(point1.x)
console.log(point2.x)

console.log(point1.x == point2.x);