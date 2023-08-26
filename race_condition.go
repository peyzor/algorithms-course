package main

import (
	"fmt"
	"sync"
)

func main() {
	counter := 0
	var wg sync.WaitGroup
	var mu sync.Mutex

	wg.Add(1)
	go func() {
		defer wg.Done()
		for i := 0; i < 10000000; i++ {
			mu.Lock()
			counter += 1
			mu.Unlock()
		}
	}()

	wg.Add(1)
	go func() {
		defer wg.Done()
		for i := 0; i < 10000000; i++ {
			mu.Lock()
			counter -= 1
			mu.Unlock()
		}
	}()

	wg.Wait()
	fmt.Println(counter)
}
