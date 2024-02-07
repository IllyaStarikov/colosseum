import Foundation

class LinkedList<T: CustomStringConvertible & Equatable>: CustomStringConvertible {
    private class Node {
        var next: Node?
        var data: T

        init(_ data: T) {
            self.data = data
            self.next = nil
        }
    }

    private var head: Node?

    var description: String {
        if let head = head {
            return toString(head)
        }

        return ""
    }

    init(_ data: T) {
        self.head = Node(data)
    }

    init() {
        self.head = nil
    }

    private func getTail(from node: Node) -> Node {
        if let next = node.next {
            return getTail(from: next)
        }

        return node
    }

    private func toString(_ node: Node, _ current: String = "") -> String {
        if let next = node.next {
            return "\(current)\(node.data), \(toString(next, current))"
        }

        return "\(node.data)"
    }

    public func removeDuplicates() {
        func removeDuplicates(from node: Node, buffer: LinkedList<T>) {
            if !buffer.contains(node.data) {
                buffer.append(element: node.data)
            }

            if let next = node.next {
                removeDuplicates(from: next, buffer: buffer)
            }

            self.head = buffer.head
        }

        if let head = head {
            removeDuplicates(from: head, buffer: LinkedList<T>())
        }
    }

    public func contains(_ element: T) -> Bool {
        func contains(element: T, node: Node) -> Bool {
            if element == node.data {
                return true
            } else if let next = node.next {
                return contains(element: element, node: next)
            }

            return false
        }

        if let head = head {
            return contains(element: element, node: head)
        } else {
            return false
        }
    }

    public func append(element: T) {
        if let head = head {
            getTail(from: head).next = Node(element)
        } else {
            head = Node(element)
        }
    }
}
var list = LinkedList<String>()

assert(!list.contains("hello"))

list.append(element: "hello")
list.append(element: "world")
list.append(element: "world 2")
list.append(element: "world 3")
list.append(element: "world")
list.append(element: "world 4")

assert(list.contains("hello"))
assert(list.contains("world 4"))
assert(list.contains("world"))
assert(!list.contains("world something"))

list.removeDuplicates()

print(list)
