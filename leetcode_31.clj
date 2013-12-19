(use 'clojure.string)

(defn solution [s]
  (let [s (lower-case 
           (replace s #"\W" ""))]
    (if (= s
           (reverse s))
      true
      false)))

(assert
 (= (solution "A man, a plan, a canal: Panama")
    true))

(assert
 (= (solution "race a car")
    false))

(assert
 (= (solution " ")
    true))

(println "Pass!")
