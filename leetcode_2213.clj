(defn solution [coll]
  (let [l (count coll)
        mid (int (/ l 2))
        s (mod l 2)
        result (interleave (take mid coll)
                           (reverse (nthrest coll
                                             (- l mid))))]
    (if (= s 1)
      (concat result
              [(nth coll mid)])
      result)))

(assert
 (= (solution '(1 2 3 4 5))
    '(1 5 2 4 3)))

(assert
 (= (solution '(1 2 3 4))
    '(1 4 2 3)))

(println "Pass!")
