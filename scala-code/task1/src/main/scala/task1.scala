object task1 {
  def main(args: Array[String]): Unit = {
    var a : Array[Int] = Array(2,3,3,4)

    var r : Seq[Seq[Int]] = Seq();

    do {
      r = r ++ Seq(a.toSeq)
    } while (next(a))

    Console.print(r)
  }

  def next(A : Array[Int]): Boolean = {
    var i : Int = A.length - 1
    while(i > 0 && A(i-1) >= A(i)) {
      i = i - 1;
    }

    if (i <= 0) return false;

    var j:Int = A.length-1;
    while(A(j) <= A(i-1)) {
      j = j-1;
    }

    var temp:Int = A(i-1)
    A(i-1) = A(j);
    A(j) = temp;

    j = A.length - 1

    while(i<j) {
      temp = A(i)
      A(i) = A(j)
      A(j) = temp
      i = i + 1
      j = j - 1
    }

    true
  }
}
