;; Extra Scheme Questions ;;

; Q5
(define (square x) (* x x))

(define (pow b n)
  'YOUR-CODE-HERE
)

; Q6
(define lst
    (list (list 1)
        (list 2 
            (list 
                (list 3 4) 
                (list 5))))
)

; Q7
(define (composed f g)
    (lambda (x) 
        (f (g x)))
)

; Q8
(define (remove item lst)
    (cond ((null? lst) '())
        ((eq? item (car lst)) (remove item (cdr lst)))
        (else (cons (car lst) (remove item (cdr lst))))
        )
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

; Q9
(define (max a b) (if (> a b) a b))
(define (min a b) (if (> a b) b a))
(define (gcd a b)
  'YOUR-CODE-HERE
)

;;; Tests
(gcd 24 60)
; expect 12
(gcd 1071 462)
; expect 21

; Q10
(define (no-repeats s)
    
)

; Q11
(define (substitute s old new)
  'YOUR-CODE-HERE
)

; Q12
(define (sub-all s olds news)
  'YOUR-CODE-HERE
)