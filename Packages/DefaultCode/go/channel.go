package main

import "time"
import "fmt"

func main() {
	messages := make(chan int, 10)
	go func() {
		// producer
		val := 0
		for {
			val += 1
			fmt.Printf("Start to add value:{%d} to the messgae queue\n", val)
      messages <- val
			time.Sleep(time.Second * 2)
		}
	}()
	go func() {
		// consumer_1
    for {
      rec := <-messages
      fmt.Printf("[consumer_1] reviced message %d\n", rec)
    }
	}()
	go func() {
		// consumer_2
    for {
      rec := <-messages
      fmt.Printf("[consumer_2] reviced message %d\n", rec)
    }
	}()
	time.Sleep(time.Hour * 8)
}

